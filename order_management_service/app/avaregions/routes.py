
from typing import List
from fastapi import APIRouter, Body
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import app.avaregions.models as models
import app.avaregions.crud as crud 
from app.avaregions.schemas import AvaregionCreate , Avaregion
from app.database import SessionLocal, engine
from app.global_schemas import ResponseModel , ResponseModelSchema
 


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



router = APIRouter()



@router.get("/regions/{goveID}" )
def get_all_avaregionsz_by_gov(goveID:int , skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    avaregions = crud.get_avaregion_by_gove(db, skip , limit  , goveID  )
    return avaregions


@router.get("/", response_model=List[Avaregion])
def get_all_avaregions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    avaregions = crud.get_avaregions(db, skip=skip, limit=limit)
    return avaregions

@router.post("/", response_model=Avaregion)
def create_avaregion(avaregion: AvaregionCreate, db: Session = Depends(get_db)):
    return crud.create_avaregion(db=db, avaregion=avaregion)

@router.delete("/" )
def delete_all_avaregions(db: Session = Depends(get_db)):
	db_avaregion = crud.delete_all_avaregion(db)
	raise  HTTPException(200, ResponseModel([] , "All Avaregions Deleted" , True , 200 , {})) from None

@router.get("/{ avaregion_id}", response_model=Avaregion)
def get_one_avaregion(avaregion_id: int, db: Session = Depends(get_db)):
    db_avaregion = crud.get_avaregion(db, avaregion_id=avaregion_id)
    if db_avaregion is None:
        raise HTTPException(status_code=404, detail=ResponseModel([] , " Avaregion not found" , True , 404 , {}))
    return db_avaregion

@router.put("/{id}")
def update_avaregion(id:int ,db: Session = Depends(get_db) , avaregion: AvaregionCreate = Body(...)):
	db_avaregion = crud.update_avaregion(db, avaregion   ,id)
	return  db_avaregion

@router.delete("/{id}"  )
def delete_one_avaregion(id:int ,db: Session = Depends(get_db)):
	db_avaregion = crud.delete_avaregion(db,id)
	return  db_avaregion