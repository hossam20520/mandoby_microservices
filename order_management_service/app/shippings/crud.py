
from sqlalchemy.orm import Session
from app.shippings.models import ShippingModel
from app.shippings.schemas import ShippingCreate , Shipping
from fastapi import Depends, HTTPException
from sqlalchemy.ext.declarative import DeclarativeMeta as Model
from sqlalchemy.exc import IntegrityError
from app.global_schemas import ResponseModel



def get_shippings(db: Session, skip: int = 0, limit: int = 100):
    return db.query(ShippingModel).offset(skip).limit(limit).all()


def create_shipping(db: Session, shipping:Shipping):
    try:
        db_shipping  = ShippingModel(**shipping.dict())
        db.add(db_shipping)
        db.commit()
        db.refresh(db_shipping)
    except IntegrityError:
         db.rollback()
         raise HTTPException(422, ResponseModel([] , "Shipping already exist" , False , 422 , {"error":"Already exists"})) from None
    return db_shipping


def delete_all_shipping(db: Session):
    db.query(ShippingModel).delete()
    db.commit()
    return []


def get_shipping(db: Session, shipping_id: int):
    return db.query(ShippingModel).filter(ShippingModel.id == shipping_id).first()


def get_shipping_by_email(db: Session, email: str):
    return db.query(ShippingModel).filter(ShippingModel.email == email).first()

def update_shipping(db: Session , shipping: dict , id: int):
   db.query(ShippingModel).filter(ShippingModel.id == id).update(dict(shipping), synchronize_session = False)
   db.commit()
   return shipping


def delete_shipping(db: Session , id:int):
    db_model = db.query(ShippingModel).get(id)
    if db_model:
         db.delete(db_model)
         db.commit() 
         return db_model
            
    else:
          raise HTTPException(status_code=404, detail=ResponseModel([] , "Shipping not found" , True , 404 , {}))
