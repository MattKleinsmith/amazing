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
    title = Column(VARCHAR(400), nullable=False)
    price = Column(DECIMAL, nullable=False)
    description = Column(TEXT)

    created_at = Column(DateTime(timezone=True),
                        server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True),
                        server_default=func.now(), onupdate=func.now(),
                        nullable=False)

    seller = relationship("User", back_populates="products")
    product_images = relationship(
        "ProductImage", cascade="all, delete-orphan", back_populates="product", order_by="ProductImage.id")
    reviews = relationship(
        "Review", back_populates="product", cascade="all, delete-orphan")

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "price": str(self.price),
            "description": self.description,
            "seller": self.seller.to_dict(),
        }

    def to_dict_search_results(self):
        preview_images = list(filter(lambda x: x.preview, self.product_images))
        avg_rating = sum(
            [review.rating for review in self.reviews]) / len(self.reviews) if len(self.reviews) > 0 else None
        num_ratings = len(self.reviews)
        return {
            "id": self.id,

            "title": self.title,
            "price": str(self.price),

            "avg_rating": avg_rating,
            "num_ratings": num_ratings,
            "preview_image": preview_images[-1].url if len(preview_images) else None,
        }

    def to_dict_details(self):
        avg_rating = sum(
            [review.rating for review in self.reviews]) / len(self.reviews) if len(self.reviews) > 0 else None
        num_ratings = len(self.reviews)
        product_images = list(
            filter(lambda x: not x.preview, self.product_images))
        return {
            "id": self.id,
            "seller_id": self.seller_id,

            "title": self.title,
            "price": str(self.price),
            "description": self.description,

            "seller": self.seller.to_dict_for_product(),
            "image_urls": [x.to_dict_for_product() for x in product_images],

            "avg_rating": avg_rating,
            "num_ratings": num_ratings
        }

    def to_dict_inventory(self):
        preview_images = list(filter(lambda x: x.preview, self.product_images))
        return {
            "preview_image": preview_images[-1].url if len(preview_images) else None,
            "title": self.title,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "price": self.price
        }

    def to_dict_inventory_edit(self):
        product_images = list(
            filter(lambda x: not x.preview, self.product_images))
        return {
            "image_urls": [x.to_dict_for_product() for x in product_images],
            "title": self.title,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "price": self.price,
            "description": self.description
        }
