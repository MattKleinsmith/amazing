from flask import Blueprint
from flask_login import login_required, current_user
from sqlalchemy.exc import IntegrityError

from app.models import db, ReviewImage, Review

bp = Blueprint("review_images", __name__, url_prefix="/review_images")


@bp.route("<int:review_image_id>",  methods=["DELETE"])
@login_required
def delete_review_image(review_image_id):
    try:
        image = ReviewImage.query.filter(
            ReviewImage.id == review_image_id).first()
        if image and Review.query.filter(Review.id == image.review_id, Review.buyer_id == current_user.id):
            db.session.delete(image)
            db.session.commit()
            return {"message": f"Deleted review image with id {review_image_id}"}
        return "404", 404
    except IntegrityError as e:
        return {"errors": {
            "server": "Server failed to delete"
        }}, 500
