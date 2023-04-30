
from typing import List
from fastapi import APIRouter, Body
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import app.shippings.models as models
import app.shippings.crud as crud 
from app.shippings.schemas import ShippingCreate , Shipping
from app.database import SessionLocal, engine
from app.global_schemas import ResponseModel , ResponseModelSchema



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



router = APIRouter()

@router.get("/", response_model=List[Shipping])
def get_all_shippings(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    shippings = crud.get_shippings(db, skip=skip, limit=limit)
    return shippings

@router.post("/", response_model=Shipping)
def create_shipping(shipping: ShippingCreate, db: Session = Depends(get_db)):
    return crud.create_shipping(db=db, shipping=shipping)

@router.delete("/" )
def delete_all_shippings(db: Session = Depends(get_db)):
	db_shipping = crud.delete_all_shipping(db)
	raise  HTTPException(200, ResponseModel([] , "All Shippings Deleted" , True , 200 , {})) from None

@router.get("/{ shipping_id}", response_model=Shipping)
def get_one_shipping(shipping_id: int, db: Session = Depends(get_db)):
    db_shipping = crud.get_shipping(db, shipping_id=shipping_id)
    if db_shipping is None:
        raise HTTPException(status_code=404, detail=ResponseModel([] , " Shipping not found" , True , 404 , {}))
    return db_shipping

@router.put("/{id}")
def update_shipping(id:int ,db: Session = Depends(get_db) , shipping: ShippingCreate = Body(...)):
	db_shipping = crud.update_shipping(db, shipping   ,id)
	return  db_shipping

@router.delete("/{id}"  )
def delete_one_shipping(id:int ,db: Session = Depends(get_db)):
	db_shipping = crud.delete_shipping(db,id)
	return  db_shipping