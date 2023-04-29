
from sqlalchemy.orm import Session
from app.inventorys.models import InventoryModel , ProductInventoryModel
from app.inventorys.schemas import InventoryCreate , Inventory
from fastapi import Depends, HTTPException
from sqlalchemy.ext.declarative import DeclarativeMeta as Model
from sqlalchemy.exc import IntegrityError
from app.global_schemas import ResponseModel








def get_inventorys_pagentation(db: Session, skip: int = 0, limit: int = 100):
        data = db.query(InventoryModel).order_by(InventoryModel.id.desc())
        items = data.offset(skip).limit(limit).all()
        return {"items":items , "total":data.count() }



def get_inventorys(db: Session, skip: int = 0, limit: int = 100):
    return db.query(InventoryModel).offset(skip).limit(limit).all()


def create_inventory(db: Session, inventory:Inventory):
    try:
        db_inventory  = InventoryModel(**inventory.dict())
        db.add(db_inventory)
        db.commit()
        db.refresh(db_inventory)
    except IntegrityError:
         db.rollback()
         raise HTTPException(422, ResponseModel([] , "Inventory already exist" , False , 422 , {"error":"Already exists"})) from None
    return db_inventory


def delete_all_inventory(db: Session):
    db.query(InventoryModel).delete()
    db.commit()
    return []


def get_inventory(db: Session, inventory_id: int):
    return db.query(InventoryModel).filter(InventoryModel.id == inventory_id).first()

def get_inventory_items(db: Session, inventory_id: int , product_id:int):
    return db.query(ProductInventoryModel).filter(ProductInventoryModel.inventory_id == inventory_id , ProductInventoryModel.product_id == product_id).first()


def get_inventory_by_email(db: Session, email: str):
    return db.query(InventoryModel).filter(InventoryModel.email == email).first()

def update_inventory(db: Session , inventory: dict , id: int):
   db.query(InventoryModel).filter(InventoryModel.id == id).update(dict(inventory), synchronize_session = False)
   db.commit()
   return inventory


def delete_inventory(db: Session , id:int):
    db_model = db.query(InventoryModel).get(id)
    if db_model:
         db.delete(db_model)
         db.commit() 
         return db_model
            
    else:
          raise HTTPException(status_code=404, detail=ResponseModel([] , "Inventory not found" , True , 404 , {}))
