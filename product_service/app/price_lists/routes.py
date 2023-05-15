
from typing import List
from fastapi import APIRouter, Body
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import app.price_lists.models as models
import app.price_lists.crud as crud 
from app.price_lists.schemas import Price_listCreate , Price_list
from app.database import SessionLocal, engine
from app.global_schemas import ResponseModel , ResponseModelSchema



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



router = APIRouter()


@router.get("/pagentation" )
def get_all_price_lists_pagentation(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    price_lists = crud.get_price_lists_pagentation(db, skip=skip, limit=limit)
    return price_lists



@router.get("/select" )
def get_all_price_lists_select(  db: Session = Depends(get_db)):
    price_lists = crud.get_price_lists_all(db)
    return price_lists

@router.get("/", response_model=List[Price_list])
def get_all_price_lists(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    price_lists = crud.get_price_lists(db, skip=skip, limit=limit)
    return price_lists

@router.post("/", response_model=Price_list)
def create_price_list(price_list: Price_listCreate, db: Session = Depends(get_db)):
    return crud.create_price_list(db=db, price_list=price_list)

@router.delete("/" )
def delete_all_price_lists(db: Session = Depends(get_db)):
	db_price_list = crud.delete_all_price_list(db)
	raise  HTTPException(200, ResponseModel([] , "All Price_lists Deleted" , True , 200 , {})) from None

@router.get("/{ price_list_id}", response_model=Price_list)
def get_one_price_list(price_list_id: int, db: Session = Depends(get_db)):
    db_price_list = crud.get_price_list(db, price_list_id=price_list_id)
    if db_price_list is None:
        raise HTTPException(status_code=404, detail=ResponseModel([] , " Price_list not found" , True , 404 , {}))
    return db_price_list

@router.put("/{id}")
def update_price_list(id:int ,db: Session = Depends(get_db) , price_list: Price_listCreate = Body(...)):
	db_price_list = crud.update_price_list(db, price_list   ,id)
	return  db_price_list

@router.delete("/{id}"  )
def delete_one_price_list(id:int ,db: Session = Depends(get_db)):
	db_price_list = crud.delete_price_list(db,id)
	return  db_price_list