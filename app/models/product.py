from .db import db
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.types import Integer, DateTime, VARCHAR, DECIMAL, TEXT
from sqlalchemy.sql import func


class Product(db.Model):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)

    seller_id = Column(Integer, ForeignKey(
        'users.id', name='fk_product_seller_id', ondelete='CASCADE'), nullable=False)
    title = Column(VARCHAR(140), nullable=False)
    price = Column(DECIMAL, nullable=False)
    description = Column(TEXT)

    created_at = Column(DateTime(timezone=True),
                        server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True),
                        server_default=func.now(), onupdate=func.now(),
                        nullable=False)

    seller = relationship("User", back_populates="products")

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "price": str(self.price),
            "description": self.description,
            "seller": self.seller.to_dict(),
        }
