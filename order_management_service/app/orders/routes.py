
from typing import List
from fastapi import APIRouter, Body
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import app.orders.models as models
import app.orders.crud as crud 
from app.orders.schemas import OrderCreate , Order
from app.database import SessionLocal, engine
from app.global_schemas import ResponseModel , ResponseModelSchema



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



router = APIRouter()

@router.get("/", response_model=List[Order])
def get_all_orders(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    orders = crud.get_orders(db, skip=skip, limit=limit)
    return orders

@router.post("/", response_model=Order)
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    return crud.create_order(db=db, order=order)

@router.delete("/" )
def delete_all_orders(db: Session = Depends(get_db)):
	db_order = crud.delete_all_order(db)
	raise  HTTPException(200, ResponseModel([] , "All Orders Deleted" , True , 200 , {})) from None

@router.get("/{ order_id}", response_model=Order)
def get_one_order(order_id: int, db: Session = Depends(get_db)):
    db_order = crud.get_order(db, order_id=order_id)
    if db_order is None:
        raise HTTPException(status_code=404, detail=ResponseModel([] , " Order not found" , True , 404 , {}))
    return db_order

@router.put("/{id}")
def update_order(id:int ,db: Session = Depends(get_db) , order: OrderCreate = Body(...)):
	db_order = crud.update_order(db, order   ,id)
	return  db_order

@router.delete("/{id}"  )
def delete_one_order(id:int ,db: Session = Depends(get_db)):
	db_order = crud.delete_order(db,id)
	return  db_order