
from typing import List
from fastapi import APIRouter, Body
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import app.price_list_items.models as models
import app.price_list_items.crud as crud 
from app.price_list_items.schemas import Price_list_itemCreate , Price_list_item
from app.database import SessionLocal, engine
from app.global_schemas import ResponseModel , ResponseModelSchema



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



router = APIRouter()



@router.get("/{id}")
def get_price_list_item_oneItem(id:int ,skip:int = 0 , limit:int = 100  , db: Session = Depends(get_db) ):
	db_price_list_item = crud.get_price_list_items_one(db , skip , limit , id )
	return  db_price_list_item


@router.get("/" )
def get_all_price_list_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    price_list_items = crud.get_price_list_items(db, skip=skip, limit=limit)
    return price_list_items

@router.post("/", response_model=Price_list_item)
def create_price_list_item(price_list_item: Price_list_itemCreate, db: Session = Depends(get_db)):
    return crud.create_price_list_item(db=db, price_list_item=price_list_item)

@router.delete("/" )
def delete_all_price_list_items(db: Session = Depends(get_db)):
	db_price_list_item = crud.delete_all_price_list_item(db)
	raise  HTTPException(200, ResponseModel([] , "All Price_list_items Deleted" , True , 200 , {})) from None

@router.get("/{ price_list_item_id}", response_model=Price_list_item)
def get_one_price_list_item(price_list_item_id: int, db: Session = Depends(get_db)):
    db_price_list_item = crud.get_price_list_item(db, price_list_item_id=price_list_item_id)
    if db_price_list_item is None:
        raise HTTPException(status_code=404, detail=ResponseModel([] , " Price_list_item not found" , True , 404 , {}))
    return db_price_list_item

@router.put("/{id}")
def update_price_list_item(id:int ,db: Session = Depends(get_db) , price_list_item: Price_list_itemCreate = Body(...)):
	db_price_list_item = crud.update_price_list_item(db, price_list_item   ,id)
	return  db_price_list_item

@router.delete("/{id}"  )
def delete_one_price_list_item(id:int ,db: Session = Depends(get_db)):
	db_price_list_item = crud.delete_price_list_item(db,id)
	return  db_price_list_item