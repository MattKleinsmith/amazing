from flask import Blueprint, request
from flask_login import login_required, current_user

from app.models import db, Purchase, Order, Product

bp = Blueprint("orders", __name__, url_prefix="/orders")


@bp.route("",  methods=["POST"])
@login_required
def post_order():
    body = request.get_json()
    cart = body["cart"]
    product_ids = cart.keys()

    if len(product_ids) == 0:
        return {"errors": {"error": "No products given"}}, 400

    products = Product.query.filter(Product.id.in_(product_ids)).all()

    if len(products) == 0:
        return {"errors": {"error": "No products found"}}, 404

    products_by_id = {str(product.id): product for product in products}

    seller_ids = (product.seller_id for product in products)
    if current_user.id in seller_ids:
        return {"errors": {"error": "Seller can't order their own products"}}, 401

    order = Order()

    purchases = [Purchase(order=order,
                          buyer_id=current_user.id,
                          seller_id=products_by_id[product_id].seller_id,
                          product_id=product_id,
                          address=body["address"],
                          price=products_by_id[product_id].price,
                          quantity=quantity)
                 for product_id, quantity in cart.items()]

    db.session.add_all(purchases)
    db.session.commit()
    return {"order_id": order.id}, 201
