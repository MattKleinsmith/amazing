from .db import db
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Integer, DateTime, DECIMAL, TEXT
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship


class Purchase(db.Model):
    __tablename__ = "purchases"

    id = Column(Integer, primary_key=True)

    order_id = Column(Integer, ForeignKey(
        'orders.id', name='fk_purchase_order_id', ondelete='CASCADE'))

    address = Column(TEXT)

    buyer_id = Column(Integer, ForeignKey(
        'users.id', name='fk_purchase_buyer_id', ondelete='CASCADE'), nullable=False)

    seller_id = Column(Integer, ForeignKey(
        'users.id', name='fk_purchase_seller_id', ondelete='CASCADE'), nullable=False)

    product_id = Column(Integer, ForeignKey(
        'products.id', name='fk_purchase_product_id', ondelete='CASCADE'), nullable=False)

    price = Column(DECIMAL, nullable=False)

    quantity = Column(Integer, nullable=False)

    created_at = Column(DateTime(timezone=True),
                        server_default=func.now(), nullable=False)

    order = relationship("Order")

    def to_dict(self):
        return {
            "id": self.id,
            "order_id": self.order_id,
            "seller_id": self.seller_id,
            "product_id": self.product_id,
            "price": self.price,
            "quantity": self.quantity,
            "address": self.address,
            "created_at": self.created_at
        }
