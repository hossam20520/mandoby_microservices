
from sqlalchemy.orm import Session
from app.governorates.models import GovernorateModel
from app.governorates.schemas import GovernorateCreate , Governorate
from fastapi import Depends, HTTPException
from sqlalchemy.ext.declarative import DeclarativeMeta as Model
from sqlalchemy.exc import IntegrityError
from app.global_schemas import ResponseModel



def get_governorates(db: Session, skip: int = 0, limit: int = 100):
    return db.query(GovernorateModel).offset(skip).limit(limit).all()


def create_governorate(db: Session, governorate:Governorate):
    try:
        db_governorate  = GovernorateModel(**governorate.dict())
        db.add(db_governorate)
        db.commit()
        db.refresh(db_governorate)
    except IntegrityError:
         db.rollback()
         raise HTTPException(422, ResponseModel([] , "Governorate already exist" , False , 422 , {"error":"Already exists"})) from None
    return db_governorate


def delete_all_governorate(db: Session):
    db.query(GovernorateModel).delete()
    db.commit()
    return []


def get_governorate(db: Session, governorate_id: int):
    return db.query(GovernorateModel).filter(GovernorateModel.id == governorate_id).first()


def get_governorate_by_email(db: Session, email: str):
    return db.query(GovernorateModel).filter(GovernorateModel.email == email).first()

def update_governorate(db: Session , governorate: dict , id: int):
   db.query(GovernorateModel).filter(GovernorateModel.id == id).update(dict(governorate), synchronize_session = False)
   db.commit()
   return governorate


def delete_governorate(db: Session , id:int):
    db_model = db.query(GovernorateModel).get(id)
    if db_model:
         db.delete(db_model)
         db.commit() 
         return db_model
            
    else:
          raise HTTPException(status_code=404, detail=ResponseModel([] , "Governorate not found" , True , 404 , {}))
