from flask import Blueprint
from flask_login import login_required, current_user

from app.models import Purchase

bp = Blueprint("purchases", __name__, url_prefix="/purchases")


@bp.route("/current",  methods=["GET"])
@login_required
def get_current_user_purchases():
    purchases = Purchase.query.filter(Purchase.buyer_id == current_user.id)
    result = [purchase.to_dict() for purchase in purchases]
    result.reverse()
    return result
