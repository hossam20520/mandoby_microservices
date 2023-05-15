
from sqlalchemy.orm import Session
from app.price_lists.models import Price_listModel
from app.price_lists.schemas import Price_listCreate , Price_list
from fastapi import Depends, HTTPException
from sqlalchemy.ext.declarative import DeclarativeMeta as Model
from sqlalchemy.exc import IntegrityError
from app.global_schemas import ResponseModel



        
        
        
def get_price_lists_pagentation(db: Session, skip: int = 0, limit: int = 100):
    data = db.query(Price_listModel).order_by(Price_listModel.id.desc())
    items = data.offset(skip).limit(limit).all()
    return {"items":items , "total":data.count()}


def get_price_lists_all(db: Session ):
    return db.query(Price_listModel).order_by(Price_listModel.id.desc()).all()

def get_price_lists(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Price_listModel).offset(skip).limit(limit).all()


def create_price_list(db: Session, price_list:Price_list):
    try:
        db_price_list  = Price_listModel(**price_list.dict())
        db.add(db_price_list)
        db.commit()
        db.refresh(db_price_list)
    except IntegrityError:
         db.rollback()
         raise HTTPException(422, ResponseModel([] , "Price_list already exist" , False , 422 , {"error":"Already exists"})) from None
    return db_price_list


def delete_all_price_list(db: Session):
    db.query(Price_listModel).delete()
    db.commit()
    return []


def get_price_list(db: Session, price_list_id: int):
    return db.query(Price_listModel).filter(Price_listModel.id == price_list_id).first()


def get_price_list_by_email(db: Session, email: str):
    return db.query(Price_listModel).filter(Price_listModel.email == email).first()

def update_price_list(db: Session , price_list: dict , id: int):
   db.query(Price_listModel).filter(Price_listModel.id == id).update(dict(price_list), synchronize_session = False)
   db.commit()
   return price_list


def delete_price_list(db: Session , id:int):
    db_model = db.query(Price_listModel).get(id)
    if db_model:
         db.delete(db_model)
         db.commit() 
         return db_model
            
    else:
          raise HTTPException(status_code=404, detail=ResponseModel([] , "Price_list not found" , True , 404 , {}))
