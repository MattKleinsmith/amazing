from flask import Blueprint, request
from flask_login import login_required, current_user
from app.models import db, Product
from app.forms import ProductForm, validation_errors_formatter
from sqlalchemy.exc import IntegrityError

bp = Blueprint("products", __name__, url_prefix="/products")


@bp.route("",  methods=["GET"])
def get_products():
    terms = request.args.get("k")
    if terms:
        terms = terms.split("+")
        products = []
        for term in terms:
            products = Product.query.filter(Product.title.match(term)).all()
            products += Product.query.filter(
                Product.description.match(term)).all()
        return [product.to_dict_search_results() for product in set(products)]
    return [product.to_dict_search_results() for product in Product.query]


@bp.route("/current",  methods=["GET"])
def get_current_products():
    return [product.to_dict_inventory() for product in Product.query.filter(Product.seller_id == current_user.id)]


@bp.route("<int:product_id>",  methods=["GET"])
def get_product(product_id):
    try:
        product = Product.query.get(product_id)
        return product.to_dict_details() if product else (f"Product with id {product_id} not found", 404)
    except Exception:
        return "500", 500


@bp.route("",  methods=["POST"])
@login_required
def post_product():
    form = ProductForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if (form.validate_on_submit()):
        product = Product(
            seller=current_user,
            title=form.title.data,
            price=form.price.data,
            description=form.description.data
        )
        db.session.add(product)
        db.session.commit()
        return product.to_dict(), 201
    return {'errors': validation_errors_formatter(form, form.errors)}, 400


@bp.route("<int:product_id>",  methods=["PUT"])
def put_product(product_id):
    product = Product.query.filter(Product.id == product_id,
                                   Product.seller_id == current_user.id).first()
    if (not product):
        return "404", 404
    form = ProductForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        product.title = form.title.data
        product.price = form.price.data
        product.description = form.description.data
        db.session.commit()
        return product.to_dict()
    return {'errors': validation_errors_formatter(form, form.errors)}, 400


@bp.route("<int:product_id>",  methods=["DELETE"])
def delete_product(product_id):
    try:
        product = db.session.query(Product).filter(
            Product.id == product_id, Product.seller_id == current_user.id).first()
        if (product):
            db.session.delete(product)
            db.session.commit()
            return {"message": f"Deleted product with id {product_id}"}
        return "404", 404
    except IntegrityError as e:
        return {"errors": {
            "server": "Server failed to delete"
        }}, 500
