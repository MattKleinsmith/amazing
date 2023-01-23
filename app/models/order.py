from .db import db
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Integer, TEXT, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

class Order(db.Model):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    address = Column(TEXT)
    created_at = Column(DateTime(timezone=True),
                        server_default=func.now(), nullable=False)
    buyer_id = Column(Integer,
                      ForeignKey('users.id', name='fk_order_buyer_id', ondelete='CASCADE'),
                      nullable=False)

    purchases = relationship("Purchase", back_populates="order")
