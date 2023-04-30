
from typing import List
from fastapi import APIRouter, Body
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import app.payments.models as models
import app.payments.crud as crud 
from app.payments.schemas import PaymentCreate , Payment
from app.database import SessionLocal, engine
from app.global_schemas import ResponseModel , ResponseModelSchema



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



router = APIRouter()

@router.get("/", response_model=List[Payment])
def get_all_payments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    payments = crud.get_payments(db, skip=skip, limit=limit)
    return payments

@router.post("/", response_model=Payment)
def create_payment(payment: PaymentCreate, db: Session = Depends(get_db)):
    return crud.create_payment(db=db, payment=payment)

@router.delete("/" )
def delete_all_payments(db: Session = Depends(get_db)):
	db_payment = crud.delete_all_payment(db)
	raise  HTTPException(200, ResponseModel([] , "All Payments Deleted" , True , 200 , {})) from None

@router.get("/{ payment_id}", response_model=Payment)
def get_one_payment(payment_id: int, db: Session = Depends(get_db)):
    db_payment = crud.get_payment(db, payment_id=payment_id)
    if db_payment is None:
        raise HTTPException(status_code=404, detail=ResponseModel([] , " Payment not found" , True , 404 , {}))
    return db_payment

@router.put("/{id}")
def update_payment(id:int ,db: Session = Depends(get_db) , payment: PaymentCreate = Body(...)):
	db_payment = crud.update_payment(db, payment   ,id)
	return  db_payment

@router.delete("/{id}"  )
def delete_one_payment(id:int ,db: Session = Depends(get_db)):
	db_payment = crud.delete_payment(db,id)
	return  db_payment