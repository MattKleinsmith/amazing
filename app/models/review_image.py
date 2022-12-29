from .db import db
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.types import Integer, DateTime, TEXT, BOOLEAN
from sqlalchemy.sql import func


class ReviewImage(db.Model):
    __tablename__ = "review_images"

    id = Column(Integer, primary_key=True)

    review_id = Column(Integer, ForeignKey(
        'reviews.id', name='fk_review_image_review_id', ondelete='CASCADE'), nullable=False)
    url = Column(TEXT, nullable=False)

    created_at = Column(DateTime(timezone=True),
                        server_default=func.now(), nullable=False)

    review = relationship(
        "Review", back_populates="review_images")  # For seeding

    def to_dict(self):
        return {
            "id": self.id,
            "review_id": self.review_id,
            "url": self.url,
        }
