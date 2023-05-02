
from typing import List
from fastapi import APIRouter, Body , Header
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import app.addresses.models as models
import app.addresses.crud as crud 
from app.addresses.schemas import AddresseCreate , Addresse
from app.database import SessionLocal, engine
from app.global_schemas import ResponseModel , ResponseModelSchema
from app.auth.auth import Auth


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



router = APIRouter()
@router.get("/my/addresses")
def get_one_addresse_by_user(  db: Session = Depends(get_db) , token:str = Header()):
    auth = Auth()
    auth.accessToken(token)
    user = auth.getUserInfo()
    
    db_addresse = crud.get_addresse_by_user(db, user['id'])
    if db_addresse is None:
        raise HTTPException(status_code=404, detail=ResponseModel([] , " Addresse not found" , True , 404 , {}))
    return db_addresse




@router.put("/")
def update_addresse_by_user( db: Session = Depends(get_db) , token:str = Header()):
    auth = Auth()
    auth.accessToken(token)
    user = auth.getUserInfo()
    db_addresse = crud.update_addresse_by_user(db, user['id'])
    return  db_addresse


@router.get("/", response_model=List[Addresse])
def get_all_addresses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    addresses = crud.get_addresses(db, skip=skip, limit=limit)
    return addresses



@router.post("/", response_model=Addresse)
def create_addresse(addresse: AddresseCreate, db: Session = Depends(get_db)):
    return crud.create_addresse(db=db, addresse=addresse)

@router.delete("/" )
def delete_all_addresses(db: Session = Depends(get_db)):
	db_addresse = crud.delete_all_addresse(db)
	raise  HTTPException(200, ResponseModel([] , "All Addresses Deleted" , True , 200 , {})) from None

@router.get("/{ addresse_id}", response_model=Addresse)
def get_one_addresse(addresse_id: int, db: Session = Depends(get_db)):
    db_addresse = crud.get_addresse(db, addresse_id=addresse_id)
    if db_addresse is None:
        raise HTTPException(status_code=404, detail=ResponseModel([] , " Addresse not found" , True , 404 , {}))
    return db_addresse

@router.put("/{id}")
def update_addresse(id:int ,db: Session = Depends(get_db) , addresse: AddresseCreate = Body(...)):
	db_addresse = crud.update_addresse(db, addresse   ,id)
	return  db_addresse

@router.delete("/{id}"  )
def delete_one_addresse(id:int ,db: Session = Depends(get_db)):
	db_addresse = crud.delete_addresse(db,id)
	return  db_addresse