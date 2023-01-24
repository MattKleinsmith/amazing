from flask import Blueprint, request
from flask_login import login_required, current_user
from sqlalchemy.exc import IntegrityError

from app.models import db, CartItem
from app.forms import validation_errors_formatter, CartItemForm

bp = Blueprint("cart_items", __name__, url_prefix="/cart_items")


@bp.route("",  methods=["POST"])
@login_required
def post_cart_item():
    """CREATE"""
    form = CartItemForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if (form.validate_on_submit()):
        cart_item = CartItem(
            user_id=current_user.id,
            product_id=form.product_id.data,
            quantity=form.quantity.data,
        )
        db.session.add(cart_item)
        db.session.commit()
        return cart_item.to_dict(), 201
    return {'errors': validation_errors_formatter(form, form.errors)}, 400

@bp.route("",  methods=["GET"])
@login_required
def get_cart_items():
    """READ"""
    return CartItem.query.filter(CartItem.user_id == current_user.id)

@bp.route("",  methods=["PUT"])
@login_required
def put_cart_item():
    """UPDATE"""
    cart_item = CartItem.query.filter(CartItem.product_id == form.product_id.data,
                                   CartItem.user_id == current_user.id).first()
    if (not cart_item):
        return "404", 404
    form = CartItem()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        cart_item.quantity = form.quantity.data
        db.session.commit()
        return cart_item.to_dict()
    return {'errors': validation_errors_formatter(form, form.errors)}, 400


@bp.route("<int:product_id>",  methods=["DELETE"])
@login_required
def delete_cart_item(product_id):
    """DELETE"""
    try:
        cart_item = CartItem.query.filter(CartItem.product_id == product_id,
                                    CartItem.user_id == current_user.id).first()
        if cart_item:
            db.session.delete(cart_item)
            db.session.commit()
            return {"message": f"Deleted cart item with product id {product_id}"}
        return "404", 404
    except IntegrityError as e:
        return {"errors": {
            "server": "Server failed to delete"
        }}, 500
