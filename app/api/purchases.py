from flask import Blueprint
from flask_login import login_required, current_user

from app.models import Order

bp = Blueprint("purchases", __name__, url_prefix="/purchases")


@bp.route("/current",  methods=["GET"])
@login_required
def get_current_user_purchases():
    orders = Order.query.filter(Order.buyer_id == current_user.id).all()
    result = [[purchase.to_dict() for purchase in order.purchases] for order in orders]
    result.reverse()
    return result
