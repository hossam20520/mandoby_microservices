
from typing import List
from fastapi import APIRouter, Body
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import app.units.models as models
import app.units.crud as crud 
from app.units.schemas import UnitCreate , Unit
from app.database import SessionLocal, engine
from app.global_schemas import ResponseModel , ResponseModelSchema



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



router = APIRouter()

@router.get("/", response_model=List[Unit])
def get_all_units(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    units = crud.get_units(db, skip=skip, limit=limit)
    return units

@router.post("/", response_model=Unit)
def create_unit(unit: UnitCreate, db: Session = Depends(get_db)):
    return crud.create_unit(db=db, unit=unit)

@router.delete("/" )
def delete_all_units(db: Session = Depends(get_db)):
	db_unit = crud.delete_all_unit(db)
	raise  HTTPException(200, ResponseModel([] , "All Units Deleted" , True , 200 , {})) from None

@router.get("/{ unit_id}", response_model=Unit)
def get_one_unit(unit_id: int, db: Session = Depends(get_db)):
    db_unit = crud.get_unit(db, unit_id=unit_id)
    if db_unit is None:
        raise HTTPException(status_code=404, detail=ResponseModel([] , " Unit not found" , True , 404 , {}))
    return db_unit

@router.put("/{id}")
def update_unit(id:int ,db: Session = Depends(get_db) , unit: UnitCreate = Body(...)):
	db_unit = crud.update_unit(db, unit   ,id)
	return  db_unit

@router.delete("/{id}"  )
def delete_one_unit(id:int ,db: Session = Depends(get_db)):
	db_unit = crud.delete_unit(db,id)
	return  db_unit