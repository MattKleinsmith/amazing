from .db import db
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Integer, DECIMAL
from sqlalchemy.orm import relationship


class Purchase(db.Model):
    __tablename__ = "purchases"

    id = Column(Integer, primary_key=True)

    order_id = Column(Integer, ForeignKey(
        'orders.id', name='fk_purchase_order_id', ondelete='CASCADE'))

    seller_id = Column(Integer, ForeignKey(
        'users.id', name='fk_purchase_seller_id', ondelete='CASCADE'), nullable=False)

    product_id = Column(Integer, ForeignKey(
        'products.id', name='fk_purchase_product_id', ondelete='CASCADE'), nullable=False)

    price = Column(DECIMAL, nullable=False)

    quantity = Column(Integer, nullable=False)

    order = relationship("Order", back_populates="purchases")

    def to_dict(self):
        return {
            "id": self.id,
            "order_id": self.order_id,
            "seller_id": self.seller_id,
            "product_id": self.product_id,
            "price": self.price,
            "quantity": self.quantity,
            "address": self.order.address,
            "created_at": self.order.created_at
        }
