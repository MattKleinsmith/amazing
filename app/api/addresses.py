from flask import Blueprint, request
from flask_login import login_required, current_user
from sqlalchemy.exc import IntegrityError

from app.models import db, Address
from app.forms import AddressForm, validation_errors_formatter

bp = Blueprint("addresses", __name__, url_prefix="/addresses")


@bp.route("",  methods=["POST"])
@login_required
def post_address():
    form = AddressForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if (form.validate_on_submit()):
        address = Address(
            user_id=current_user.id,
            fullname=form.fullname.data,
            address=form.address.data,
            building=form.building.data,
            city=form.city.data,
            state=form.state.data,
            zipcode=form.zipcode.data,
            region=form.region.data,
            phone=form.phone.data
        )

        db.session.add(address)
        db.session.commit()
        return address.to_dict(), 201
    return {'errors': validation_errors_formatter(form, form.errors)}, 400


@bp.route("/current",  methods=["GET"])
def get_current_user_addresses():
    addresses = Address.query.filter(Address.user_id == current_user.id)
    return [address.to_dict() for address in addresses]


@bp.route("<int:address_id>",  methods=["PUT"])
@login_required
def put_address(address_id):
    address = Address.query.filter(Address.id == address_id,
                                   Address.user_id == current_user.id).first()
    if (not address):
        return "404", 404
    form = AddressForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        address.fullname = form.fullname.data
        address.address = form.address.data
        address.building = form.building.data
        address.city = form.city.data
        address.state = form.state.data
        address.zipcode = form.zipcode.data
        address.region = form.region.data
        address.phone = form.phone.data
        db.session.commit()
        return address.to_dict()
    return {'errors': validation_errors_formatter(form, form.errors)}, 400


@bp.route("<int:address_id>",  methods=["DELETE"])
@login_required
def delete_product(address_id):
    try:
        address = db.session.query(Address).filter(
            Address.id == address_id, Address.user_id == current_user.id).first()
        if address:
            db.session.delete(address)
            db.session.commit()
            return {"message": f"Deleted address with id {address_id}"}
        return "404", 404
    except IntegrityError as e:
        return {"errors": {
            "server": "Server failed to delete"
        }}, 500
