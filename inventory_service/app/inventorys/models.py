
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


class InventoryModel(Base , TrackTimeMixin  , SoftDeleteMixin ):
    __tablename__ = "inventorys"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(192))
    statut = Column(Boolean, default=True)
    image = Column(String(200))


class ProductInventoryModel(Base , TrackTimeMixin  , SoftDeleteMixin ):
    __tablename__ = "product_inventorys"
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, index=True)
    inventory_id = Column(Integer, index=True)
    product_variant_id = Column(Integer, index=True, nullable=True)
    qty = Column(Float(precision=10))

