
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


class PaymentModel(Base , TrackTimeMixin ):
    __tablename__ = "payments"
    id = Column(Integer, primary_key=True, index=True)
    user_id  = Column(Integer, nullable=True, index=True)
    shop_id  = Column(Integer, nullable=True, index=True)
    order_id  = Column(Integer, nullable=True, index=True)
    payment_status  = Column(Integer, nullable=True, index=True)
    paid =  Column(Integer, nullable=True, index=True)
    payment_method = Column(Integer, nullable=True, index=True)
    




class PaymentMethodsModel(Base , TrackTimeMixin ):
    __tablename__ = "payments"
    id = Column(Integer, primary_key=True, index=True)
    ar_title = Column(String(50))
    en_title = Column(String(50))




class PaymentStatusModel(Base , TrackTimeMixin ):
    __tablename__ = "payments"
    id = Column(Integer, primary_key=True, index=True)
    ar_title = Column(String(50))
    en_title = Column(String(50))
    
    