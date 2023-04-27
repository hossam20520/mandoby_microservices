from typing import List ,  Annotated
from fastapi import APIRouter, Body
from fastapi import Depends, FastAPI, HTTPException ,  UploadFile , File ,Form
from sqlalchemy.orm import Session
import app.categorys.models as models
import app.categorys.crud as crud 
from app.categorys.schemas import CategoryCreate , Category
from app.database import SessionLocal, engine
from app.global_schemas import ResponseModel , ResponseModelSchema
import time
import os 
from fastapi.responses import FileResponse
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



router = APIRouter()


# async def create_upload_file(file: UploadFile , fileb: Annotated[UploadFile, File()] ,  token: Annotated[str, Form()]):

@router.post("/image/")
async def create_upload_file(file: UploadFile):
    timestamp = time.strftime('%H%M%Y%m%d')
    timestamp2 = time.strftime('%S%M%Y%m%d')
    current_dir = os.getcwd()
    file_name, file_ext = os.path.splitext(file.filename)
    new_file_name = f"{timestamp}{timestamp2}{file_ext}"
    file_location = f"{current_dir}/media/category/{new_file_name}"
    if not os.path.exists('/app/media/category'):
          os.makedirs('/app/media/category')
    with open(file_location, "wb+") as file_object:
          file_object.write(file.file.read())
          print(os.getcwd())
    return {"image": new_file_name}



@router.get("/get/image")
def get_image_category(name:str):
     current_dir = os.getcwd()
     file_location = f"{current_dir}/media/category/{name}"
     if os.path.exists(file_location):
          file_location = f"{current_dir}/media/category/{name}"
          return FileResponse(file_location , status_code=200)
     else:
         file_location = f"{current_dir}/media/default.png"
         return FileResponse(file_location , status_code=404)


@router.get("/pagenation")
def get_all_categorys(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    categorys = crud.get_categorys_pagentation(db, skip=skip, limit=limit)
    return categorys

@router.get("/", response_model=List[Category])
def get_all_categorys(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    categorys = crud.get_categorys(db, skip=skip, limit=limit)
    return categorys

@router.post("/", response_model=Category)
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    return crud.create_category(db=db, category=category)

@router.delete("/" )
def delete_all_categorys(db: Session = Depends(get_db)):
	db_category = crud.delete_all_category(db)
	raise  HTTPException(200, ResponseModel([] , "All Categorys Deleted" , True , 200 , {})) from None

@router.get("/{category_id}", response_model=Category)
def get_one_category(category_id: int, db: Session = Depends(get_db)):
    db_category = crud.get_category(db, category_id=category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail=ResponseModel([] , " Category not found" , True , 404 , {}))
    return db_category

@router.put("/{id}")
def update_category(id:int ,db: Session = Depends(get_db) , category: CategoryCreate = Body(...)):
	db_category = crud.update_category(db, category   ,id)
	return  db_category

@router.delete("/{id}"  )
def delete_one_category(id:int ,db: Session = Depends(get_db)):
	db_category = crud.delete_category(db,id)
	return  db_category