from flask import Blueprint, request
from flask_login import login_required, current_user

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
            city=form.city.data,
            state=form.state.data,
            zipcode=form.zipcode.data,
            region=form.region.data
        )

        db.session.add(address)
        db.session.commit()
        return address.to_dict(), 201
    return {'errors': validation_errors_formatter(form, form.errors)}, 400


@bp.route("/current",  methods=["GET"])
def get_current_user_addresses():
    addresses = Address.query.filter(Address.user_id == current_user.id)
    return [address.to_dict() for address in addresses]
