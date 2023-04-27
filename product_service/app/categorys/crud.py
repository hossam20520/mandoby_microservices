
from sqlalchemy.orm import Session
from app.categorys.models import CategoryModel
from app.categorys.schemas import CategoryCreate , Category
from fastapi import Depends, HTTPException
from sqlalchemy.ext.declarative import DeclarativeMeta as Model
from sqlalchemy.exc import IntegrityError
from app.global_schemas import ResponseModel




def get_categorys_pagentation(db: Session, skip: int = 0, limit: int = 100):
        data = db.query(CategoryModel).order_by(CategoryModel.id.desc())
        items = data.offset(skip).limit(limit).all()
        return {"items":items , "total":data.count() }


def get_categorys(db: Session, skip: int = 0, limit: int = 100):
    return db.query(CategoryModel).offset(skip).limit(limit).all()


def create_category(db: Session, category:Category):
    try:
        db_category  = CategoryModel(**category.dict())
        db.add(db_category)
        db.commit()
        db.refresh(db_category)
    except IntegrityError:
         db.rollback()
         raise HTTPException(422, ResponseModel([] , "Category already exist" , False , 422 , {"error":"Already exists"})) from None
    return db_category


def delete_all_category(db: Session):
    db.query(CategoryModel).delete()
    db.commit()
    return []


def get_category(db: Session, category_id: int):
    return db.query(CategoryModel).filter(CategoryModel.id == category_id).first()


def get_category_by_email(db: Session, email: str):
    return db.query(CategoryModel).filter(CategoryModel.email == email).first()

def update_category(db: Session , category: dict , id: int):
   db.query(CategoryModel).filter(CategoryModel.id == id).update(dict(category), synchronize_session = False)
   db.commit()
   return category


def delete_category(db: Session , id:int):
    db_model = db.query(CategoryModel).get(id)
    if db_model:
         db.delete(db_model)
         db.commit() 
         return db_model
            
    else:
          raise HTTPException(status_code=404, detail=ResponseModel([] , "Category not found" , True , 404 , {}))
