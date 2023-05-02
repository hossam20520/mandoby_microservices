
from sqlalchemy.orm import Session
from app.addresses.models import AddresseModel
from app.addresses.schemas import AddresseCreate , Addresse
from app.avagovs.models import AvagovModel
from app.avaregions.models import AvaregionModel
from fastapi import Depends, HTTPException
from sqlalchemy.ext.declarative import DeclarativeMeta as Model
from sqlalchemy.exc import IntegrityError
from app.global_schemas import ResponseModel
from sqlalchemy import desc


def get_addresses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(AddresseModel).offset(skip).limit(limit).all()


def update_addresse_by_user(db: Session ,   id: int):
   addresse:dict  = {"selected": False}
   db.query(AddresseModel).filter(AddresseModel.user_id == id).update(dict(addresse), synchronize_session = False)
   db.commit()
   return addresse




def create_addresse(db: Session, addresse:Addresse):
    try:
        db_addresse  = AddresseModel(**addresse.dict())
        db.add(db_addresse)
        db.commit()
        db.refresh(db_addresse)
    except IntegrityError:
         db.rollback()
         raise HTTPException(422, ResponseModel([] , "Addresse already exist" , False , 422 , {"error":"Already exists"})) from None
    return db_addresse





def delete_all_addresse(db: Session):
    db.query(AddresseModel).delete()
    db.commit()
    return []

def get_addresse_by_user(db: Session, userid: int):
    addresses = db.query(AddresseModel , AvagovModel , AvaregionModel ).join(AvagovModel, AvagovModel.id == AddresseModel.govern_id).join(AvaregionModel , AvaregionModel.id == AddresseModel.region_id).filter(AddresseModel.user_id == userid).order_by(desc(AddresseModel.id)).all()
    selected = db.query(AddresseModel , AvagovModel , AvaregionModel ).join(AvagovModel, AvagovModel.id == AddresseModel.govern_id).join(AvaregionModel , AvaregionModel.id == AddresseModel.region_id).filter(AddresseModel.user_id == userid).filter(AddresseModel.selected == True).first()
    return {"addresses":addresses , "selected":selected}



def get_addresse(db: Session, addresse_id: int):
    return db.query(AddresseModel).filter(AddresseModel.id == addresse_id).first()


def get_addresse_by_email(db: Session, email: str):
    return db.query(AddresseModel).filter(AddresseModel.email == email).first()

def update_addresse(db: Session , addresse: dict , id: int):
   db.query(AddresseModel).filter(AddresseModel.id == id).update(dict(addresse), synchronize_session = False)
   db.commit()
   return addresse


def delete_addresse(db: Session , id:int):
    db_model = db.query(AddresseModel).get(id)
    if db_model:
         db.delete(db_model)
         db.commit() 
         return db_model
            
    else:
          raise HTTPException(status_code=404, detail=ResponseModel([] , "Addresse not found" , True , 404 , {}))
