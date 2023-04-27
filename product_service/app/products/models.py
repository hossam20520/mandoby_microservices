
from datetime import datetime
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String , DateTime , Float
from sqlalchemy.orm import relationship
from app.database import Base
from sqlalchemy.sql import func
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class TrackTimeMixin:

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=datetime.now)

class SoftDeleteMixin:
    deleted_at = Column(DateTime, nullable=True)

    def soft_delete(self):
        self.deleted_at = datetime.now()


class ProductModel(Base , TrackTimeMixin , SoftDeleteMixin ):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    en_title = Column(String(100))
    ar_title = Column(String(100))
    slug     = Column(String(100))
    code     = Column(String(100))
    Type_barcode = Column(String(50) , nullable=True)
    price = Column(Float(precision=10, asdecimal=False))
    cost = Column(Float(precision=10, asdecimal=False))
    category_id  = Column(Integer, ForeignKey("categorys.id") , index=True)
    unit_id = Column(Integer, ForeignKey("units.id") , nullable=True)
    unit_sale_id = Column(Integer, ForeignKey("units.id") , nullable=True)
    unit_purchase_id = Column(Integer, ForeignKey("units.id") , nullable=True)
    TaxNet  = Column(Float(precision=10, asdecimal=False) , nullable=True, default=0)
    tax_method  = Column(String(50) , default= '1')
    image = Column(String(200) , nullable=True)
    note  = Column(String(200) , nullable=True)
    stock_alert = Column(Float(precision=10, asdecimal=False), nullable=True, default=0)
    is_variant = Column(Boolean, default=False)
    is_active = Column(Boolean, default=False)
   
    