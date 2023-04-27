
from sqlalchemy.orm import Session
from gateways.models import GatewayModel
from gateways.schemas import GatewayCreate , Gateway
from fastapi import Depends, HTTPException
from sqlalchemy.ext.declarative import DeclarativeMeta as Model
from sqlalchemy.exc import IntegrityError
from global_schemas import ResponseModel



def get_gateways(db: Session, skip: int = 0, limit: int = 100):
    return db.query(GatewayModel).offset(skip).limit(limit).all()


def create_gateway(db: Session, gateway:Gateway):
    try:
        db_gateway  = GatewayModel(**gateway.dict())
        db.add(db_gateway)
        db.commit()
        db.refresh(db_gateway)
    except IntegrityError:
         db.rollback()
         raise HTTPException(422, ResponseModel([] , "Gateway already exist" , False , 422 , {"error":"Already exists"})) from None
    return db_gateway


def delete_all_gateway(db: Session):
    db.query(GatewayModel).delete()
    db.commit()
    return []


def get_gateway(db: Session, gateway_id: int):
    return db.query(GatewayModel).filter(GatewayModel.id == gateway_id).first()


def get_gateway_by_email(db: Session, email: str):
    return db.query(GatewayModel).filter(GatewayModel.email == email).first()

def update_gateway(db: Session , gateway: dict , id: int):
   db.query(GatewayModel).filter(GatewayModel.id == id).update(dict(gateway), synchronize_session = False)
   db.commit()
   return gateway


def delete_gateway(db: Session , id:int):
    db_model = db.query(GatewayModel).get(id)
    if db_model:
         db.delete(db_model)
         db.commit() 
         return db_model
            
    else:
          raise HTTPException(status_code=404, detail=ResponseModel([] , "Gateway not found" , True , 404 , {}))
