
from typing import List
from fastapi import APIRouter, Body
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import app.governorates.models as models
import app.governorates.crud as crud 
from app.governorates.schemas import GovernorateCreate , Governorate
from app.database import SessionLocal, engine
from app.global_schemas import ResponseModel , ResponseModelSchema



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



router = APIRouter()

@router.get("/", response_model=List[Governorate])
def get_all_governorates(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    governorates = crud.get_governorates(db, skip=skip, limit=limit)
    return governorates

@router.post("/", response_model=Governorate)
def create_governorate(governorate: GovernorateCreate, db: Session = Depends(get_db)):
    return crud.create_governorate(db=db, governorate=governorate)

@router.delete("/" )
def delete_all_governorates(db: Session = Depends(get_db)):
	db_governorate = crud.delete_all_governorate(db)
	raise  HTTPException(200, ResponseModel([] , "All Governorates Deleted" , True , 200 , {})) from None

@router.get("/{ governorate_id}", response_model=Governorate)
def get_one_governorate(governorate_id: int, db: Session = Depends(get_db)):
    db_governorate = crud.get_governorate(db, governorate_id=governorate_id)
    if db_governorate is None:
        raise HTTPException(status_code=404, detail=ResponseModel([] , " Governorate not found" , True , 404 , {}))
    return db_governorate

@router.put("/{id}")
def update_governorate(id:int ,db: Session = Depends(get_db) , governorate: GovernorateCreate = Body(...)):
	db_governorate = crud.update_governorate(db, governorate   ,id)
	return  db_governorate

@router.delete("/{id}"  )
def delete_one_governorate(id:int ,db: Session = Depends(get_db)):
	db_governorate = crud.delete_governorate(db,id)
	return  db_governorate