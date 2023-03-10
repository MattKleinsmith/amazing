from .db import db
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Integer, DateTime, VARCHAR
from sqlalchemy.sql import func


class Address(db.Model):
    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer,
                     ForeignKey('users.id', name='fk_address_user_id',
                                ondelete='CASCADE'),
                     nullable=False)

    fullname = Column(VARCHAR(1000), nullable=False)
    address = Column(VARCHAR(1000), nullable=False)
    building = Column(VARCHAR(1000))
    city = Column(VARCHAR(1000), nullable=False)
    state = Column(VARCHAR(1000))
    zipcode = Column(VARCHAR(1000), nullable=False)
    region = Column(VARCHAR(1000), nullable=False)
    phone = Column(VARCHAR(1000), nullable=False)

    created_at = Column(DateTime(timezone=True),
                        server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True),
                        server_default=func.now(), onupdate=func.now(),
                        nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "fullname": self.fullname,
            "address": self.address,
            "building": self.building,
            "city": self.city,
            "state": self.state,
            "zipcode": self.zipcode,
            "region": self.region,
            "phone": self.phone
        }
