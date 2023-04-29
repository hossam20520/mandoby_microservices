
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



class UnitModel(Base , TrackTimeMixin  , SoftDeleteMixin):
    __tablename__ = "units"
    id = Column(Integer, primary_key=True, index=True)
    en_title = Column(String(50))
    ar_title = Column(String(50))
    ShortName = Column(String(50))
    base_unit =  Column(Integer, nullable=True, index=True)
    operator =  Column(String(192), nullable=True, default='*')
    operator_value = Column(Float(precision=10, asdecimal=False), nullable=True, default=1)