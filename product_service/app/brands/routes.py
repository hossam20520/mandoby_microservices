
from typing import List
from fastapi import APIRouter, Body
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import app.brands.models as models
import app.brands.crud as crud 
from app.brands.schemas import BrandCreate , Brand
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
def get_brands_pagenation(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    brands = crud.get_brand_pagentation(db, skip=skip, limit=limit)
    return brands

@router.get("/", response_model=List[Brand])
def get_all_brands(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    brands = crud.get_brands(db, skip=skip, limit=limit)
    return brands

@router.post("/", response_model=Brand)
def create_brand(brand: BrandCreate, db: Session = Depends(get_db)):
    return crud.create_brand(db=db, brand=brand)

@router.delete("/" )
def delete_all_brands(db: Session = Depends(get_db)):
	db_brand = crud.delete_all_brand(db)
	raise  HTTPException(200, ResponseModel([] , "All Brands Deleted" , True , 200 , {})) from None

@router.get("/{ brand_id}", response_model=Brand)
def get_one_brand(brand_id: int, db: Session = Depends(get_db)):
    db_brand = crud.get_brand(db, brand_id=brand_id)
    if db_brand is None:
        raise HTTPException(status_code=404, detail=ResponseModel([] , " Brand not found" , True , 404 , {}))
    return db_brand

@router.put("/{id}")
def update_brand(id:int ,db: Session = Depends(get_db) , brand: BrandCreate = Body(...)):
	db_brand = crud.update_brand(db, brand   ,id)
	return  db_brand

@router.delete("/{id}"  )
def delete_one_brand(id:int ,db: Session = Depends(get_db)):
	db_brand = crud.delete_brand(db,id)
	return  db_brand