from flask import Blueprint, request
from flask_login import login_required, current_user
from app.models import db, Product


bp = Blueprint("products", __name__, url_prefix="/products")


@bp.route("",  methods=["POST"])
def post_product():
    return "post_product"


@bp.route("",  methods=["GET"])
def get_products():
    return "get_products"


@bp.route("<int:product_id>",  methods=["GET"])
def get_product(product_id):
    return "get_products"


@bp.route("<int:product_id>",  methods=["PUT"])
def put_product(product_id):
    return "put_product"


@bp.route("<int:product_id>",  methods=["DELETE"])
def delete_product(product_id):
    return "delete_product"
