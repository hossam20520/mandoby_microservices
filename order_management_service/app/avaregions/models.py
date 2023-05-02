
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




class AvaregionModel(Base , TrackTimeMixin , SoftDeleteMixin ):
    __tablename__ = "avaregions"
    id = Column(Integer, primary_key=True, index=True)
    gov_id = Column(Integer, nullable=True, index=True)
    ar_title = Column(String(50))
    en_title = Column(String(50))
    code = Column(String(50))
    lat  = Column(String(100) , nullable=True)
    long = Column(String(100) , nullable=True)
    ava = Column(Boolean, default=True)
    deleted = Column(Boolean, default=False)



    