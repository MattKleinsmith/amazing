from .db import db
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Integer

class CartItem(db.Model):
    __tablename__ = "cart_items"

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer,
                      ForeignKey('users.id', name='fk_cart_item_user_id', ondelete='CASCADE'),
                      nullable=False)
    product_id = Column(Integer,
                      ForeignKey('products.id', name='fk_cart_item_product_id', ondelete='CASCADE'),
                      nullable=False)
    quantity = Column(Integer)

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "product_id": self.product_id,
            "quantity": self.quantity
        }
