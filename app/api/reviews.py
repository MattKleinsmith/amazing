from flask import Blueprint, request
from flask_login import login_required, current_user
from sqlalchemy.exc import IntegrityError

from app.models import db, Review
from app.forms import ReviewForm, validation_errors_formatter

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
