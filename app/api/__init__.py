from flask import Blueprint
from . import orders, session, users, products, addresses, product_images, purchases, reviews, review_images

bp = Blueprint("api", __name__, url_prefix="/api")

bp.register_blueprint(users.bp)
bp.register_blueprint(session.bp)
bp.register_blueprint(products.bp)
bp.register_blueprint(addresses.bp)
bp.register_blueprint(product_images.bp)
bp.register_blueprint(orders.bp)
bp.register_blueprint(purchases.bp)
bp.register_blueprint(reviews.bp)
bp.register_blueprint(review_images.bp)
