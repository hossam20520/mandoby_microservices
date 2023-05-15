from typing import List
from fastapi import APIRouter, Body
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import app.products.models as models
import app.products.crud as crud 
from app.products.schemas import ProductCreate , Product
from app.database import SessionLocal, engine
from app.global_schemas import ResponseModel , ResponseModelSchema
from app.products.relations.products import ProductsC
from app.services.InventoryService import InventoryService

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



router = APIRouter()


@router.get("/pagentation" )
def get_all_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    products = crud.get_product_pagentation(db, skip=skip, limit=limit)
    return products




@router.get("/select" )
def get__moble_all_products_select( db: Session = Depends(get_db)):
    data = crud.get_all_products( db )
    return data


@router.get("/dashboard/pagentation" )
def get__moble_all_products_dash(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    # products = crud.get_product_pagentation(db, skip=skip, limit=limit)
    # pro = ProductsC(db )
    data = crud.getProducts( db , skip=skip , limit=limit)
    return data

@router.get("/mobile/pagentation" )
def get__moble_all_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    # products = crud.get_product_pagentation(db, skip=skip, limit=limit)
    pro = ProductsC(db )
    data = pro.getProducts( skip=skip , limit=limit)
    return data


@router.get("/category/{category_id}/" )
def get_all_products_by_category(category_id:int  , skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    products = crud.get_product_pagentation_category(db, skip ,  limit  , category_id )
    return products



@router.get("/", response_model=List[Product])
def get_all_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    products = crud.get_products(db, skip=skip, limit=limit)
    return products

@router.post("/", response_model=Product)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db=db, product=product)

@router.delete("/" )
def delete_all_products(db: Session = Depends(get_db)):
	db_product = crud.delete_all_product(db)
	raise  HTTPException(200, ResponseModel([] , "All Products Deleted" , True , 200 , {})) from None

@router.get("/{product_id}")
def get_one_product(product_id: int, db: Session = Depends(get_db)):
    db_product = crud.get_product(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail=ResponseModel([] , " Product not found" , True , 404 , {}))
    
    # 1 - Inventory Service
    # invent = InventoryService()
    # stock = invent.ProductNumInventory(1,product_id)
    # if stock.status_code == 200:
         
    #      stock = stock.json()
    # else:
    #     stock = []
    # End Inventory Service 
    # product = {
    #      "product":db_product 
    # }
    return db_product 

@router.put("/{id}")
def update_product(id:int ,db: Session = Depends(get_db) , product: ProductCreate = Body(...)):
	db_product = crud.update_product(db, product   ,id)
	return  db_product

@router.delete("/{id}"  )
def delete_one_product(id:int ,db: Session = Depends(get_db)):
	db_product = crud.delete_product(db,id)
	return  db_product