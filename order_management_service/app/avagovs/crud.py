
from sqlalchemy.orm import Session
from app.avagovs.models import AvagovModel
from app.avagovs.schemas import AvagovCreate , Avagov
from fastapi import Depends, HTTPException
from sqlalchemy.ext.declarative import DeclarativeMeta as Model
from sqlalchemy.exc import IntegrityError
from app.global_schemas import ResponseModel



def get_avagovs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(AvagovModel).offset(skip).limit(limit).all()



def get_avagovs_pagentaion(db: Session, skip: int = 0, limit: int = 100 , av:bool = True):
    data = db.query(AvagovModel).filter(AvagovModel.ava == av ).order_by(AvagovModel.id.desc())
    items = data.offset(skip).limit(limit).all()
    return {"items":items , "total":data.count() }

    
   

def create_avagov(db: Session, avagov:Avagov):
    try:
        db_avagov  = AvagovModel(**avagov.dict())
        db.add(db_avagov)
        db.commit()
        db.refresh(db_avagov)
    except IntegrityError:
         db.rollback()
         raise HTTPException(422, ResponseModel([] , "Avagov already exist" , False , 422 , {"error":"Already exists"})) from None
    return db_avagov


def delete_all_avagov(db: Session):
    db.query(AvagovModel).delete()
    db.commit()
    return []


def get_avagov(db: Session, avagov_id: int):
    return db.query(AvagovModel).filter(AvagovModel.id == avagov_id).first()


def get_avagov_by_email(db: Session, email: str):
    return db.query(AvagovModel).filter(AvagovModel.email == email).first()

def update_avagov(db: Session , avagov: dict , id: int):
   db.query(AvagovModel).filter(AvagovModel.id == id).update(dict(avagov), synchronize_session = False)
   db.commit()
   return avagov


def delete_avagov(db: Session , id:int):
    db_model = db.query(AvagovModel).get(id)
    if db_model:
         db.delete(db_model)
         db.commit() 
         return db_model
            
    else:
          raise HTTPException(status_code=404, detail=ResponseModel([] , "Avagov not found" , True , 404 , {}))
