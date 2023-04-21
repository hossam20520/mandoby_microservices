
from sqlalchemy.orm import Session
from app.permissions.models import PermissionModel
from app.permissions.schemas import PermissionCreate , Permission
from fastapi import Depends, HTTPException
from sqlalchemy.ext.declarative import DeclarativeMeta as Model
from sqlalchemy.exc import IntegrityError
from app.global_schemas import ResponseModel



def get_permissions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(PermissionModel).offset(skip).limit(limit).all()


def create_permission(db: Session, permission:Permission):
    try:
        db_permission  = PermissionModel(**permission.dict())
        db.add(db_permission)
        db.commit()
        db.refresh(db_permission)
    except IntegrityError:
         db.rollback()
         raise HTTPException(422, ResponseModel([] , "Permission already exist" , False , 422 , {"error":"Already exists"})) from None
    return db_permission


def delete_all_permission(db: Session):
    db.query(PermissionModel).delete()
    db.commit()
    return []


def get_permission(db: Session, permission_id: int):
    return db.query(PermissionModel).filter(PermissionModel.id == permission_id).first()


def get_permission_by_email(db: Session, email: str):
    return db.query(PermissionModel).filter(PermissionModel.email == email).first()

def update_permission(db: Session , permission: dict , id: int):
   db.query(PermissionModel).filter(PermissionModel.id == id).update(dict(permission), synchronize_session = False)
   db.commit()
   return permission


def delete_permission(db: Session , id:int):
    db_model = db.query(PermissionModel).get(id)
    if db_model:
         db.delete(db_model)
         db.commit() 
         return db_model
            
    else:
          raise HTTPException(status_code=404, detail=ResponseModel([] , "Permission not found" , True , 404 , {}))



def create_permission_seeds(db: Session, data):
    for items in data:
        try:
            db_permission  = PermissionModel(**items)
            db.add(db_permission)

        except IntegrityError:
            db.rollback()
            raise HTTPException(422, ResponseModel([] , "Permission already exist" , False , 422 , {"error":"Already exists"})) from None
    db.commit()             
    db.refresh(db_permission)
    raise HTTPException(200, ResponseModel([] , "Success Seed" , False , 200 , {})) from None