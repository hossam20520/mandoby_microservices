
from sqlalchemy.orm import Session
from app.order_managements.models import Order_managementModel
from app.order_managements.schemas import Order_managementCreate , Order_management
from fastapi import Depends, HTTPException
from sqlalchemy.ext.declarative import DeclarativeMeta as Model
from sqlalchemy.exc import IntegrityError
from app.global_schemas import ResponseModel



def get_order_managements(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Order_managementModel).offset(skip).limit(limit).all()


def create_order_management(db: Session, order_management:Order_management):
    try:
        db_order_management  = Order_managementModel(**order_management.dict())
        db.add(db_order_management)
        db.commit()
        db.refresh(db_order_management)
    except IntegrityError:
         db.rollback()
         raise HTTPException(422, ResponseModel([] , "Order_management already exist" , False , 422 , {"error":"Already exists"})) from None
    return db_order_management


def delete_all_order_management(db: Session):
    db.query(Order_managementModel).delete()
    db.commit()
    return []


def get_order_management(db: Session, order_management_id: int):
    return db.query(Order_managementModel).filter(Order_managementModel.id == order_management_id).first()


def get_order_management_by_email(db: Session, email: str):
    return db.query(Order_managementModel).filter(Order_managementModel.email == email).first()

def update_order_management(db: Session , order_management: dict , id: int):
   db.query(Order_managementModel).filter(Order_managementModel.id == id).update(dict(order_management), synchronize_session = False)
   db.commit()
   return order_management


def delete_order_management(db: Session , id:int):
    db_model = db.query(Order_managementModel).get(id)
    if db_model:
         db.delete(db_model)
         db.commit() 
         return db_model
            
    else:
          raise HTTPException(status_code=404, detail=ResponseModel([] , "Order_management not found" , True , 404 , {}))
