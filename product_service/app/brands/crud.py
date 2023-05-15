
from sqlalchemy.orm import Session
from app.brands.models import BrandModel
from app.brands.schemas import BrandCreate , Brand
from fastapi import Depends, HTTPException
from sqlalchemy.ext.declarative import DeclarativeMeta as Model
from sqlalchemy.exc import IntegrityError
from app.global_schemas import ResponseModel



def get_brands(db: Session, skip: int = 0, limit: int = 100):
    return db.query(BrandModel).offset(skip).limit(limit).all()


def get_brand_pagentation(db: Session, skip: int = 0, limit: int = 100):
        data = db.query(BrandModel).order_by(BrandModel.id.desc())
        items = data.offset(skip).limit(limit).all()
        return {"items":items , "total":data.count() }

 

def create_brand(db: Session, brand:Brand):
    try:
        db_brand  = BrandModel(**brand.dict())
        db.add(db_brand)
        db.commit()
        db.refresh(db_brand)
    except IntegrityError:
         db.rollback()
         raise HTTPException(422, ResponseModel([] , "Brand already exist" , False , 422 , {"error":"Already exists"})) from None
    return db_brand


def delete_all_brand(db: Session):
    db.query(BrandModel).delete()
    db.commit()
    return []


def get_brand(db: Session, brand_id: int):
    return db.query(BrandModel).filter(BrandModel.id == brand_id).first()


def get_brand_by_email(db: Session, email: str):
    return db.query(BrandModel).filter(BrandModel.email == email).first()

def update_brand(db: Session , brand: dict , id: int):
   db.query(BrandModel).filter(BrandModel.id == id).update(dict(brand), synchronize_session = False)
   db.commit()
   return brand


def delete_brand(db: Session , id:int):
    db_model = db.query(BrandModel).get(id)
    if db_model:
         db.delete(db_model)
         db.commit() 
         return db_model
            
    else:
          raise HTTPException(status_code=404, detail=ResponseModel([] , "Brand not found" , True , 404 , {}))
