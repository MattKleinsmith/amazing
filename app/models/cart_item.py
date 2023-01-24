from .db import db
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Integer

class CartItem(db.Model):
    __tablename__ = "cart_items"

    user_id = Column(Integer,
                      ForeignKey('users.id', name='fk_cart_item_user_id', ondelete='CASCADE'),
                      nullable=False)
    product_id = Column(Integer,
                      ForeignKey('products.id', name='fk_cart_item_product_id', ondelete='CASCADE'),
                      nullable=False)
    quantity = Column(Integer)
