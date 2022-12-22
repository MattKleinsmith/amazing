from .db import db
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.types import Integer, DateTime, TEXT, BOOLEAN
from sqlalchemy.sql import func


class ProductImage(db.Model):
    __tablename__ = "product_images"

    id = Column(Integer, primary_key=True)

    product_id = Column(Integer, ForeignKey(
        'products.id', name='fk_product_image_product_id', ondelete='CASCADE'), nullable=False)
    url = Column(TEXT, nullable=False)
    preview = Column(BOOLEAN, nullable=False)

    created_at = Column(DateTime(timezone=True),
                        server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True),
                        server_default=func.now(), onupdate=func.now(),
                        nullable=False)

    product = relationship(
        "Product", back_populates="product_images")  # For seeding

    def to_dict(self):
        return {
            "id": self.id,
            "product_id": self.product_id,
            "url": self.url,
            "preview": self.preview
        }

    def to_dict_for_product(self):
        return self.url
