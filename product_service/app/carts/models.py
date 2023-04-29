
from datetime import datetime
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String , DateTime , Float
from sqlalchemy.orm import relationship
from app.database import Base
from sqlalchemy.sql import func
from app.products.models import ProductModel
from sqlalchemy.orm import joinedload
class TrackTimeMixin:

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=datetime.now)

class SoftDeleteMixin:
    deleted_at = Column(DateTime, nullable=True)

    def soft_delete(self):
        self.deleted_at = datetime.now()


class CartModel(Base , TrackTimeMixin , SoftDeleteMixin ):
    __tablename__ = "carts"
    id = Column(Integer, primary_key=True, index=True)
    total = Column(Float, default=0.0)
    discount = Column(Float(precision=10, asdecimal=False) , default=0.0)
    user_id = Column(Integer , nullable=True , index=True)
    order_id = Column(Integer , nullable=True , default=0 , index=True)
   




class CartItemModel(Base , TrackTimeMixin  ,SoftDeleteMixin ):
    __tablename__ = 'cart_items'
    id = Column(Integer, primary_key=True)
    cart_id = Column(Integer,nullable=True , default=0 , index=True )
    product_id = Column(Integer,nullable=True , default=0 , index=True )
    quantity = Column(Integer)
    price = Column(Float(precision=10, asdecimal=False))
    subtotal = Column(Float(precision=10, asdecimal=False))
    # def join_product():
    #     return joinedload(CartItemModel.product)
    

    # @property
    # def product(self):
    #     query = ProductModel.query
    #     query = query.filter(ProductModel.id == self.product_id)
    #     return query.first()