
from sqlalchemy.orm import Session
from app.regions.models import RegionModel
from app.regions.schemas import RegionCreate , Region
from fastapi import Depends, HTTPException
from sqlalchemy.ext.declarative import DeclarativeMeta as Model
from sqlalchemy.exc import IntegrityError
from app.global_schemas import ResponseModel



def get_regions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(RegionModel).offset(skip).limit(limit).all()


def create_region(db: Session, region:Region):
    try:
        db_region  = RegionModel(**region.dict())
        db.add(db_region)
        db.commit()
        db.refresh(db_region)
    except IntegrityError:
         db.rollback()
         raise HTTPException(422, ResponseModel([] , "Region already exist" , False , 422 , {"error":"Already exists"})) from None
    return db_region


def delete_all_region(db: Session):
    db.query(RegionModel).delete()
    db.commit()
    return []


def get_region(db: Session, region_id: int):
    return db.query(RegionModel).filter(RegionModel.id == region_id).first()


def get_region_by_email(db: Session, email: str):
    return db.query(RegionModel).filter(RegionModel.email == email).first()

def update_region(db: Session , region: dict , id: int):
   db.query(RegionModel).filter(RegionModel.id == id).update(dict(region), synchronize_session = False)
   db.commit()
   return region


def delete_region(db: Session , id:int):
    db_model = db.query(RegionModel).get(id)
    if db_model:
         db.delete(db_model)
         db.commit() 
         return db_model
            
    else:
          raise HTTPException(status_code=404, detail=ResponseModel([] , "Region not found" , True , 404 , {}))
