from .db import db
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer


class Order(db.Model):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
