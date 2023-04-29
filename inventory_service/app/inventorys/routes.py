
from typing import List
from fastapi import APIRouter, Body
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import app.inventorys.models as models
import app.inventorys.crud as crud 
from app.inventorys.schemas import InventoryCreate , Inventory
from app.database import SessionLocal, engine
from app.global_schemas import ResponseModel , ResponseModelSchema



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



router = APIRouter()





@router.get("/numbers/{inventory_id}/{product_id}" )
def get_one_inventory_data(inventory_id: int,  product_id:int , db: Session = Depends(get_db)):
    db_inventory = crud.get_inventory(db, inventory_id=inventory_id)
    if db_inventory is None:
        raise HTTPException(status_code=404, detail=ResponseModel([] , "Inventory not found" , True , 404 , {}))
    
    items = crud.get_inventory_items(db ,inventory_id , product_id=product_id )
    if items is None:
        raise HTTPException(status_code=404, detail=ResponseModel([] , "Product not found" , True , 404 , {}))

    return items


@router.get("/pagentation" )
def get_all_inventorys(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    inventorys = crud.get_inventorys_pagentation(db, skip=skip, limit=limit)
    return inventorys


@router.get("/", response_model=List[Inventory])
def get_all_inventorys(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    inventorys = crud.get_inventorys(db, skip=skip, limit=limit)
    return inventorys

@router.post("/", response_model=Inventory)
def create_inventory(inventory: InventoryCreate, db: Session = Depends(get_db)):
    return crud.create_inventory(db=db, inventory=inventory)


@router.delete("/" )
def delete_all_inventorys(db: Session = Depends(get_db)):
	db_inventory = crud.delete_all_inventory(db)
	raise  HTTPException(200, ResponseModel([] , "All Inventorys Deleted" , True , 200 , {})) from None

@router.get("/{inventory_id}", response_model=Inventory)
def get_one_inventory(inventory_id: int, db: Session = Depends(get_db)):
    db_inventory = crud.get_inventory(db, inventory_id=inventory_id)
    if db_inventory is None:
        raise HTTPException(status_code=404, detail=ResponseModel([] , " Inventory not found" , True , 404 , {}))
    return db_inventory

@router.put("/{id}")
def update_inventory(id:int ,db: Session = Depends(get_db) , inventory: InventoryCreate = Body(...)):
	db_inventory = crud.update_inventory(db, inventory   ,id)
	return  db_inventory

@router.delete("/{id}"  )
def delete_one_inventory(id:int ,db: Session = Depends(get_db)):
	db_inventory = crud.delete_inventory(db,id)
	return  db_inventory