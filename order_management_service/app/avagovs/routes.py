
from typing import List
from fastapi import APIRouter, Body
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import app.avagovs.models as models
import app.avagovs.crud as crud 
from app.avagovs.schemas import AvagovCreate , Avagov
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
def get_all_avagovs_pagentation(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    avagovs = crud.get_avagovs_pagentaion(db, skip=skip, limit=limit)
    return avagovs

@router.get("/", response_model=List[Avagov])
def get_all_avagovs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    avagovs = crud.get_avagovs(db, skip=skip, limit=limit)
    return avagovs

@router.post("/", response_model=Avagov)
def create_avagov(avagov: AvagovCreate, db: Session = Depends(get_db)):
    return crud.create_avagov(db=db, avagov=avagov)

@router.delete("/" )
def delete_all_avagovs(db: Session = Depends(get_db)):
	db_avagov = crud.delete_all_avagov(db)
	raise  HTTPException(200, ResponseModel([] , "All Avagovs Deleted" , True , 200 , {})) from None

@router.get("/{ avagov_id}", response_model=Avagov)
def get_one_avagov(avagov_id: int, db: Session = Depends(get_db)):
    db_avagov = crud.get_avagov(db, avagov_id=avagov_id)
    if db_avagov is None:
        raise HTTPException(status_code=404, detail=ResponseModel([] , " Avagov not found" , True , 404 , {}))
    return db_avagov

@router.put("/{id}")
def update_avagov(id:int ,db: Session = Depends(get_db) , avagov: AvagovCreate = Body(...)):
	db_avagov = crud.update_avagov(db, avagov   ,id)
	return  db_avagov

@router.delete("/{id}"  )
def delete_one_avagov(id:int ,db: Session = Depends(get_db)):
	db_avagov = crud.delete_avagov(db,id)
	return  db_avagov