from flask import Blueprint, request
from flask_login import login_required, current_user
from sqlalchemy.exc import IntegrityError

from app.models import db, Review, ReviewImage
from app.forms import ReviewForm, validation_errors_formatter
from werkzeug.utils import secure_filename
from app.seeds.upload import upload_image_to_bucket, allowed_file

bp = Blueprint("reviews", __name__, url_prefix="/reviews")


@bp.route("<int:review_id>",  methods=["PUT"])
@login_required
def put_review(review_id):
    review = Review.query.filter(Review.id == review_id,
                                 Review.buyer_id == current_user.id).first()
    if (not review):
        return "404", 404
    form = ReviewForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        review.rating = form.rating.data
        review.title = form.title.data
        review.review = form.review.data
        db.session.commit()
        return review.to_dict()
    return {'errors': validation_errors_formatter(form, form.errors)}, 400


@bp.route("<int:review_id>",  methods=["DELETE"])
@login_required
def delete_review(review_id):
    try:
        review = db.session.query(Review).filter(
            Review.id == review_id, Review.buyer_id == current_user.id).first()
        if review:
            db.session.delete(review)
            db.session.commit()
            return {"message": f"Deleted review with id {review_id}"}
        return "404", 404
    except IntegrityError as e:
        return {"errors": {
            "server": "Server failed to delete"
        }}, 500


@bp.route("<int:review_id>/images", methods=['POST'])
@login_required
def post_image_by_review_id(review_id):
    try:
        file = request.files['image']
        filename = secure_filename(file.filename)
        if not allowed_file(filename):
            return {
                "errors": {
                    "image": "Please upload a supported image format: .png and .jpg"
                }
            }, 400
        url = upload_image_to_bucket(file, filename)
        review_image = ReviewImage(
            review_id=review_id,
            url=url,
        )
        db.session.add(review_image)
        db.session.commit()
        return review_image.to_dict()
    except Exception as e:
        return {
            "errors": {
                "image": str(e)
            }
        }, 500
