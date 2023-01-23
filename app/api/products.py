from flask import Blueprint, request
from flask_login import login_required, current_user
from sqlalchemy.exc import IntegrityError
from werkzeug.utils import secure_filename

from app.models import db, Product, ProductImage, Review
from app.forms import ProductForm, ReviewForm, validation_errors_formatter
from app.seeds.upload import upload_image_to_bucket, allowed_file

bp = Blueprint("products", __name__, url_prefix="/products")


@bp.route("",  methods=["GET"])
def get_products():
    terms = request.args.get("k")
    size = request.args.get("size")
    size = size if size else 24  # Default size
    reverse = request.args.get("reverse")
    if terms:
        terms = terms.split("+")
        products = []
        for term in terms:
            products = Product.query.filter(
                Product.title.match(term)).order_by(Product.id.desc() if reverse else Product.id.asc()).limit(size).all()
            size = int(size) - len(products)
            products += Product.query.filter(
                Product.description.match(term)).order_by(Product.id.desc() if reverse else Product.id.asc()).limit(size).all()
        return [product.to_dict_search_results() for product in set(products)]
    return [product.to_dict_search_results() for product in Product.query.order_by(Product.id.desc() if reverse else Product.id.asc()).limit(size)]


@bp.route("/current",  methods=["GET"])
@login_required
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
@login_required
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
@login_required
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


@bp.route("<int:product_id>/images", methods=['POST'])
@login_required
def post_image_by_product_id(product_id):
    try:
        file = request.files['image']
        filename = secure_filename(file.filename)  # "Big Cat.jpg" -> "Big_Cat.jpg" or "../cat.jpg" -> "cat.jpg"
        if not allowed_file(filename):
            return {
                "errors": {
                    "image": "Please upload a supported image format: .png and .jpg"
                }
            }, 400
        url = upload_image_to_bucket(file, filename)
        product_image = ProductImage(
            product_id=product_id,
            url=url,
            preview=request.form['preview'] == 'true',
            position=request.form['position'] if request.form['position'] else None
        )
        if request.form['preview'] == 'true':
            # There can only be one previous image.
            preview_images = ProductImage.query.filter(
                ProductImage.preview == 't', ProductImage.product_id == product_id).all()
            for img in preview_images:
                if (img.position):
                    img.preview = False
                    # Move old preview image to the end of the list of images
                    img.position = ProductImage.query.filter(
                        ProductImage.product_id == product_id, ProductImage.position > 0).count() + 1
                else:
                    db.session.delete(img)
        db.session.add(product_image)
        db.session.commit()
        return product_image.to_dict()
    except Exception as e:
        return {
            "errors": {
                "image": str(e)
            }
        }, 500


@bp.route("<int:product_id>/reviews",  methods=["POST"])
@login_required
def post_review(product_id):
    product = Product.query.get(product_id)
    form = ReviewForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if (form.validate_on_submit()):
        review = Review(
            product=product,
            buyer=current_user,
            title=form.title.data,
            rating=form.rating.data,
            review=form.review.data
        )
        db.session.add(review)
        db.session.commit()
        return review.to_dict(), 201
    return {'errors': validation_errors_formatter(form, form.errors)}, 400


@bp.route("<int:product_id>/reviews",  methods=["GET"])
def get_reviews_for_product(product_id):
    product = Product.query.get(product_id)
    if (not product):
        return f"Product with id {product_id} not found", 404
    return [review.to_dict() for review in Review.query.filter(Review.product == product)]


@bp.route("<int:product_id>/reviews/current",  methods=["GET"])
def get_review_for_product_by_current_user(product_id):
    product = Product.query.get(product_id)
    if (not product):
        return f"Product with id {product_id} not found", 404
    review = Review.query.filter(
        Review.product == product, Review.buyer == current_user).first()
    return review.to_dict() if review else ({"error": f"Review for this product not found for this user"}, 404)
