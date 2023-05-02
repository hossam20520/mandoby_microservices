
from datetime import datetime
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String , DateTime
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


class AddresseModel(Base , TrackTimeMixin , SoftDeleteMixin ):
    __tablename__ = "addresses"
    id = Column(Integer, primary_key=True, index=True)
    user_id =  Column(Integer, nullable=True, index=True)
    lat =  Column(String(300) , nullable=True,)
    long =  Column(String(300) , nullable=True,)
    name = Column(String(50))
    address = Column(String(50))
    govern_id =  Column(Integer, nullable=True, index=True)
    govern_name = Column(String(50))
    region = Column(String(50))
    region_id =  Column(Integer, nullable=True, index=True)
    mobile = Column(String(50))
    notes = Column(String(200))
    selected = Column(Boolean, default=False)
    deleted = Column(Boolean, default=False)

