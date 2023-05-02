
from datetime import datetime
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String , DateTime , Float
from sqlalchemy.orm import relationship
from app.database import Base
from sqlalchemy.sql import func

class TrackTimeMixin:

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=datetime.now)

class SoftDeleteMixin:
    deleted_at = Column(DateTime, nullable=True)

    def soft_delete(self):
        self.deleted_at = datetime.now()


class OrderModel(Base , TrackTimeMixin , SoftDeleteMixin ):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    address_id = Column(Integer, nullable=True, index=True )
    order_number = Column(String(300) , nullable=True,)
    user_id = Column(Integer, nullable=True, index=True )
    person_delevery_id = Column(Integer, nullable=True, index=True )
    order_date = Column(DateTime, server_default=func.now())
    shop_id =   Column(Integer, nullable=True, index=True , default=0)
    payment_id =   Column(Integer, nullable=True, index=True  )
    shipping_id = Column(Integer, nullable=True, index=True , default=0)
    cart_id =   Column(Integer, nullable=True, index=True  )
    tax =   Column(Float(precision=10, asdecimal=False))
    shipping_price = Column(Float(precision=10, asdecimal=False))
    discount = Column(Float(precision=10, asdecimal=False))
    other_discount = Column(Float(precision=10, asdecimal=False) , default=0)
    subtotal = Column(Float(precision=10, asdecimal=False))
    total = Column(Float(precision=10, asdecimal=False))