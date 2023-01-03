from .db import db
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Integer, DateTime, DECIMAL
from sqlalchemy.sql import func


class Purchase(db.Model):
    __tablename__ = "purchases"

    id = Column(Integer, primary_key=True)

    order_id = Column(Integer, nullable=False)

    address_id = Column(Integer, ForeignKey(
        'addresses.id', name='fk_purchase_address_id', ondelete='CASCADE'))

    buyer_id = Column(Integer, ForeignKey(
        'users.id', name='fk_purchase_buyer_id', ondelete='CASCADE'), nullable=False)

    seller_id = Column(Integer, ForeignKey(
        'users.id', name='fk_purchase_seller_id', ondelete='CASCADE'), nullable=False)

    product_id = Column(Integer, ForeignKey(
        'users.id', name='fk_purchase_product_id', ondelete='CASCADE'), nullable=False)

    price = Column(DECIMAL, nullable=False)

    quantity = Column(Integer, nullable=False)

    created_at = Column(DateTime(timezone=True),
                        server_default=func.now(), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "order_id": self.order_id,
            "address_id": self.address_id,
            "buyer_id": self.buyer_id,
            "seller_id": self.seller_id,
            "product_id": self.product_id,
            "price": self.price,
            "quantity": self.quantity,
        }
