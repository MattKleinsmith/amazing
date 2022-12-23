from .db import db

from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.types import Integer, DateTime, VARCHAR
from sqlalchemy.sql import func


class Review(db.Model):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True)

    buyer_id = Column(Integer, ForeignKey(
        'users.id', name='fk_review_buyer_id', ondelete='CASCADE'), nullable=False)
    product_id = Column(Integer, ForeignKey(
        'products.id', name='fk_review_product_id', ondelete='CASCADE'), nullable=False)

    rating = Column(Integer, nullable=False)
    title = Column(VARCHAR(100))
    review = Column(VARCHAR(25000))

    created_at = Column(DateTime(timezone=True),
                        server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True),
                        server_default=func.now(), onupdate=func.now(),
                        nullable=False)

    buyer = relationship("User", foreign_keys=[buyer_id])
    product = relationship("Product", back_populates="reviews")
    review_images = relationship(
        "ReviewImage", cascade="all, delete-orphan", back_populates="review", order_by="ReviewImage.id")

    def to_dict(self):
        return {
            "id": self.id,
            "buyer_id": self.buyer_id,
            "product_id": self.product_id,

            "rating": self.rating,
            "review": self.review,

            "created_at": self.created_at,

            "buyer": self.buyer.to_dict(),
            "review_images": [x.to_dict() for x in self.review_images],
        }
