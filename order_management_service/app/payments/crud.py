
from sqlalchemy.orm import Session
from app.payments.models import PaymentModel
from app.payments.schemas import PaymentCreate , Payment
from fastapi import Depends, HTTPException
from sqlalchemy.ext.declarative import DeclarativeMeta as Model
from sqlalchemy.exc import IntegrityError
from app.global_schemas import ResponseModel



def get_payments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(PaymentModel).offset(skip).limit(limit).all()


def create_payment(db: Session, payment:Payment):
    try:
        db_payment  = PaymentModel(**payment.dict())
        db.add(db_payment)
        db.commit()
        db.refresh(db_payment)
    except IntegrityError:
         db.rollback()
         raise HTTPException(422, ResponseModel([] , "Payment already exist" , False , 422 , {"error":"Already exists"})) from None
    return db_payment


def delete_all_payment(db: Session):
    db.query(PaymentModel).delete()
    db.commit()
    return []


def get_payment(db: Session, payment_id: int):
    return db.query(PaymentModel).filter(PaymentModel.id == payment_id).first()


def get_payment_by_email(db: Session, email: str):
    return db.query(PaymentModel).filter(PaymentModel.email == email).first()

def update_payment(db: Session , payment: dict , id: int):
   db.query(PaymentModel).filter(PaymentModel.id == id).update(dict(payment), synchronize_session = False)
   db.commit()
   return payment


def delete_payment(db: Session , id:int):
    db_model = db.query(PaymentModel).get(id)
    if db_model:
         db.delete(db_model)
         db.commit() 
         return db_model
            
    else:
          raise HTTPException(status_code=404, detail=ResponseModel([] , "Payment not found" , True , 404 , {}))
