from flask import Blueprint
from . import session, users, products

bp = Blueprint("api", __name__, url_prefix="/api")

bp.register_blueprint(users.bp)
bp.register_blueprint(session.bp)
bp.register_blueprint(products.bp)