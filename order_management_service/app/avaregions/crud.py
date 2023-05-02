
from sqlalchemy.orm import Session
from app.avaregions.models import AvaregionModel
from app.avaregions.schemas import AvaregionCreate , Avaregion
from fastapi import Depends, HTTPException
from sqlalchemy.ext.declarative import DeclarativeMeta as Model
from sqlalchemy.exc import IntegrityError
from app.global_schemas import ResponseModel



def get_avaregions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(AvaregionModel).offset(skip).limit(limit).all()


def get_avaregion_by_gove(db: Session, skip:int , limit:int ,  gov_id: int):
    data = db.query(AvaregionModel).filter(AvaregionModel.gov_id == gov_id).order_by(AvaregionModel.id.desc())
    items = data.offset(skip).limit(limit).all()
    return {"items":items , "total":data.count() }



def create_avaregion(db: Session, avaregion:Avaregion):
    try:
        db_avaregion  = AvaregionModel(**avaregion.dict())
        db.add(db_avaregion)
        db.commit()
        db.refresh(db_avaregion)
    except IntegrityError:
         db.rollback()
         raise HTTPException(422, ResponseModel([] , "Avaregion already exist" , False , 422 , {"error":"Already exists"})) from None
    return db_avaregion


def delete_all_avaregion(db: Session):
    db.query(AvaregionModel).delete()
    db.commit()
    return []


def get_avaregion(db: Session, avaregion_id: int):
    return db.query(AvaregionModel).filter(AvaregionModel.id == avaregion_id).first()


def get_avaregion_by_email(db: Session, email: str):
    return db.query(AvaregionModel).filter(AvaregionModel.email == email).first()

def update_avaregion(db: Session , avaregion: dict , id: int):
   db.query(AvaregionModel).filter(AvaregionModel.id == id).update(dict(avaregion), synchronize_session = False)
   db.commit()
   return avaregion


def delete_avaregion(db: Session , id:int):
    db_model = db.query(AvaregionModel).get(id)
    if db_model:
         db.delete(db_model)
         db.commit() 
         return db_model
            
    else:
          raise HTTPException(status_code=404, detail=ResponseModel([] , "Avaregion not found" , True , 404 , {}))
