
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


class Order_managementModel(Base , TrackTimeMixin , SoftDeleteMixin  ):
    __tablename__ = "order_managements"
    id = Column(Integer, primary_key=True, index=True)

    



    