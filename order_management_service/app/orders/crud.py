
from sqlalchemy.orm import Session
from app.orders.models import OrderModel
from app.orders.schemas import OrderCreate , Order
from fastapi import Depends, HTTPException
from sqlalchemy.ext.declarative import DeclarativeMeta as Model
from sqlalchemy.exc import IntegrityError
from app.global_schemas import ResponseModel



def get_orders(db: Session, skip: int = 0, limit: int = 100):
    return db.query(OrderModel).offset(skip).limit(limit).all()


def create_order(db: Session, order:Order):
        db_order  = OrderModel(**order.dict())
        db.add(db_order)
        db.commit()
        db.refresh(db_order)
        return db_order


def delete_all_order(db: Session):
    db.query(OrderModel).delete()
    db.commit()
    return []


def get_order(db: Session, order_id: int):
    return db.query(OrderModel).filter(OrderModel.id == order_id).first()


def get_order_by_email(db: Session, email: str):
    return db.query(OrderModel).filter(OrderModel.email == email).first()

def update_order(db: Session , order: dict , id: int):
   db.query(OrderModel).filter(OrderModel.id == id).update(dict(order), synchronize_session = False)
   db.commit()
   return order


def delete_order(db: Session , id:int):
    db_model = db.query(OrderModel).get(id)
    if db_model:
         db.delete(db_model)
         db.commit() 
         return db_model
            
    else:
          raise HTTPException(status_code=404, detail=ResponseModel([] , "Order not found" , True , 404 , {}))
