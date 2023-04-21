
from typing import List
from fastapi import APIRouter, Body
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import app.regions.models as models
import app.regions.crud as crud 
from app.regions.schemas import RegionCreate , Region
from app.database import SessionLocal, engine
from app.global_schemas import ResponseModel , ResponseModelSchema



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



router = APIRouter()

@router.get("/", response_model=List[Region])
def get_all_regions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    regions = crud.get_regions(db, skip=skip, limit=limit)
    return regions

@router.post("/", response_model=Region)
def create_region(region: RegionCreate, db: Session = Depends(get_db)):
    return crud.create_region(db=db, region=region)

@router.delete("/" )
def delete_all_regions(db: Session = Depends(get_db)):
	db_region = crud.delete_all_region(db)
	raise  HTTPException(200, ResponseModel([] , "All Regions Deleted" , True , 200 , {})) from None

@router.get("/{ region_id}", response_model=Region)
def get_one_region(region_id: int, db: Session = Depends(get_db)):
    db_region = crud.get_region(db, region_id=region_id)
    if db_region is None:
        raise HTTPException(status_code=404, detail=ResponseModel([] , " Region not found" , True , 404 , {}))
    return db_region

@router.put("/{id}")
def update_region(id:int ,db: Session = Depends(get_db) , region: RegionCreate = Body(...)):
	db_region = crud.update_region(db, region   ,id)
	return  db_region

@router.delete("/{id}"  )
def delete_one_region(id:int ,db: Session = Depends(get_db)):
	db_region = crud.delete_region(db,id)
	return  db_region