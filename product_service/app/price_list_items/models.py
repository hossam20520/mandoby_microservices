
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


class Price_list_itemModel(Base , TrackTimeMixin , SoftDeleteMixin ):
    __tablename__  = "price_list_items"
    id             = Column(Integer, primary_key=True, index=True)
    price_list_id  =  Column(Integer, nullable=True, index=True)
    product_id     =  Column(Integer, nullable=True, index=True)
    new_price      =  Column(Float(precision=10, asdecimal=False))
    discount       =  Column(Float(precision=10, asdecimal=False))  
    