
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


class Price_listModel(Base , TrackTimeMixin  , SoftDeleteMixin ):
    __tablename__ = "price_lists"
    id = Column(Integer, primary_key=True, index=True)
    en_title = Column(String(100))
    ar_title = Column(String(100))
    is_active =  Column(Boolean, default=False)
    
    