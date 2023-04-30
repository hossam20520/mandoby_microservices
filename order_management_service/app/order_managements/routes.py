
from typing import List
from fastapi import APIRouter, Body
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import app.order_managements.models as models
import app.order_managements.crud as crud 
from app.order_managements.schemas import Order_managementCreate , Order_management
from app.database import SessionLocal, engine
from app.global_schemas import ResponseModel , ResponseModelSchema



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



router = APIRouter()

@router.get("/", response_model=List[Order_management])
def get_all_order_managements(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    order_managements = crud.get_order_managements(db, skip=skip, limit=limit)
    return order_managements

@router.post("/", response_model=Order_management)
def create_order_management(order_management: Order_managementCreate, db: Session = Depends(get_db)):
    return crud.create_order_management(db=db, order_management=order_management)

@router.delete("/" )
def delete_all_order_managements(db: Session = Depends(get_db)):
	db_order_management = crud.delete_all_order_management(db)
	raise  HTTPException(200, ResponseModel([] , "All Order_managements Deleted" , True , 200 , {})) from None

@router.get("/{ order_management_id}", response_model=Order_management)
def get_one_order_management(order_management_id: int, db: Session = Depends(get_db)):
    db_order_management = crud.get_order_management(db, order_management_id=order_management_id)
    if db_order_management is None:
        raise HTTPException(status_code=404, detail=ResponseModel([] , " Order_management not found" , True , 404 , {}))
    return db_order_management

@router.put("/{id}")
def update_order_management(id:int ,db: Session = Depends(get_db) , order_management: Order_managementCreate = Body(...)):
	db_order_management = crud.update_order_management(db, order_management   ,id)
	return  db_order_management

@router.delete("/{id}"  )
def delete_one_order_management(id:int ,db: Session = Depends(get_db)):
	db_order_management = crud.delete_order_management(db,id)
	return  db_order_management