
from sqlalchemy.orm import Session
from app.units.models import UnitModel
from app.units.schemas import UnitCreate , Unit
from fastapi import Depends, HTTPException
from sqlalchemy.ext.declarative import DeclarativeMeta as Model
from sqlalchemy.exc import IntegrityError
from app.global_schemas import ResponseModel



def get_units(db: Session, skip: int = 0, limit: int = 100):
    return db.query(UnitModel).offset(skip).limit(limit).all()


def create_unit(db: Session, unit:Unit):
    try:
        db_unit  = UnitModel(**unit.dict())
        db.add(db_unit)
        db.commit()
        db.refresh(db_unit)
    except IntegrityError:
         db.rollback()
         raise HTTPException(422, ResponseModel([] , "Unit already exist" , False , 422 , {"error":"Already exists"})) from None
    return db_unit


def delete_all_unit(db: Session):
    db.query(UnitModel).delete()
    db.commit()
    return []


def get_unit(db: Session, unit_id: int):
    return db.query(UnitModel).filter(UnitModel.id == unit_id).first()


def get_unit_by_email(db: Session, email: str):
    return db.query(UnitModel).filter(UnitModel.email == email).first()

def update_unit(db: Session , unit: dict , id: int):
   db.query(UnitModel).filter(UnitModel.id == id).update(dict(unit), synchronize_session = False)
   db.commit()
   return unit


def delete_unit(db: Session , id:int):
    db_model = db.query(UnitModel).get(id)
    if db_model:
         db.delete(db_model)
         db.commit() 
         return db_model
            
    else:
          raise HTTPException(status_code=404, detail=ResponseModel([] , "Unit not found" , True , 404 , {}))
