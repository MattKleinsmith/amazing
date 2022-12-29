from flask import Blueprint, request
from flask_login import login_required, current_user, login_user, logout_user
from app.forms import SignupForm, validation_errors_formatter
from app.models import db, User


bp = Blueprint("users", __name__, url_prefix="/users")


@bp.route("",  methods=["POST"])
def signup():
    if current_user.is_authenticated:
        return {"message": 'User has logged in'}
    form = SignupForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        data = form.data
        if User.query.filter(User.email == data['email']).one_or_none():
            return {'errors': {'email': "Email has already been used."}}, 400
        user = User(
            fullname=data['fullname'],
            email=data['email'],
            password=data['password']
        )
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return user.to_dict(), 201
    return {'errors': validation_errors_formatter(form, form.errors)}, 400


@bp.route("/current", methods=["DELETE"])
@login_required
def delete_user():
    """For debugging"""
    db.session.delete(current_user)
    db.session.commit()
    logout_user()
    return "Deleted user and logged out"
