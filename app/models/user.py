from .db import db
from flask_login import UserMixin
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, DateTime, VARCHAR, TEXT
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from flask_login import UserMixin
#  a crypto library that came with Flask
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)

    fullname = Column(VARCHAR(100), nullable=False)
    email = Column(VARCHAR(100), nullable=False, unique=True)
    hashed_password = Column(TEXT, nullable=False)

    created_at = Column(DateTime(timezone=True),
                        server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True),
                        server_default=func.now(), onupdate=func.now(),
                        nullable=False)

    products = relationship("Product", back_populates="seller")

    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_dict(self):
        return {
            "id": self.id,
            "fullname": self.fullname,
            "email": self.email,
        }

    def to_dict_for_product(self):
        return {
            "fullname": self.fullname,
            "email": self.email,
        }
