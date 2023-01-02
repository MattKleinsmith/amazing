from flask import Blueprint
from flask_login import login_required, current_user
from sqlalchemy.exc import IntegrityError

from app.models import db, ProductImage, Product

bp = Blueprint("product_images", __name__, url_prefix="/product_images")


@bp.route("<int:product_image_id>",  methods=["DELETE"])
@login_required
def delete_product_image(product_image_id):
    try:
        image = ProductImage.query.filter(
            ProductImage.id == product_image_id).first()
        if image and Product.query.filter(Product.id == image.product_id, Product.seller_id == current_user.id):
            other_images = ProductImage.query.filter(
                ProductImage.product_id == image.product_id, ProductImage.id != product_image_id).all()
            if (len(other_images) > 0):
                next_image = other_images[0]
                next_image.preview = True
                print("-------------setting preview image",
                      next_image.id, next_image.url, next_image.preview)
            db.session.delete(image)
            db.session.commit()
            return {"message": f"Deleted product image with id {product_image_id}"}
        return "404", 404
    except IntegrityError as e:
        return {"errors": {
            "server": "Server failed to delete"
        }}, 500
