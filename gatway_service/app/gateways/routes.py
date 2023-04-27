
from typing import List , Annotated
from fastapi import APIRouter, Body , Header
from fastapi import Depends, FastAPI, HTTPException , Form  , UploadFile , File
from sqlalchemy.orm import Session
# from app.database import SessionLocal, engine
from fastapi.security import HTTPBearer, HTTPBasicCredentials
import requests
from app.gateways.services.user_service.LoginService import LoginService
from fastapi.responses import FileResponse
import time
import os 
from app.gateways.services.product_service.Media import Media
from app.gateways.services.product_service.CategoryService import CategoryService
from app.gateways.services.product_service.ProductService import ProductService
from io import BytesIO
from app.gateways.schemas.products.schemas import CategoryCreate
from fastapi.security import HTTPBearer
from fastapi.encoders import jsonable_encoder
from app.auth.auth import Auth
router = APIRouter()



@router.post("/client/login")
def client_login_gatway(user_credentials: HTTPBasicCredentials = Body(...)):
    
    req = LoginService()
    response = req.ClientLogin(user_credentials.username ,user_credentials.password)
    return response


@router.get("/categories")
async def getCategories(skip: int = 0, limit: int = 100):
        ob = CategoryService()
        response = ob.Category(skip , limit)
        return response



@router.post("/category/image/upload")
async def UploadImageCategory(file: UploadFile):
        # url = "http://product_service:8000/api/v1.0/categorys/image/"
        # response = requests.post(url, files= file )
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
        return {"filename": new_file_name}



@router.get("/image/{filename}")
async def read_image(filename: str):
    ob = Media()
    response = ob.CategoryImage(filename)
    
    current_dir = os.getcwd()
   
    file_location = f"{current_dir}/media/category/{filename}"
    
    if os.path.exists(file_location):
        return FileResponse(file_location )
    else:
        if(response.status_code == 404):
            file_location = f"{current_dir}/media/default.png"
            return FileResponse(file_location )    
         
        with open(file_location, 'wb') as f:
            f.write(response.content)
    return FileResponse(file_location )




@router.get("/category/pagenation")
def get_category_pagentation(skip: int = 0, limit: int = 100):
    # headers = {}
    # if authorization:
    #     headers["Authorization"] = f"Bearer {authorization}"
    # Make authenticated request using the access token
    response = requests.get(f"http://product_service:8000/api/v1.0/categorys/pagenation?skip={skip}&limit={limit}" )
    return response.json()


@router.post("/category/create")
def create_category(category:CategoryCreate , token: str =  Header()):
    auth = Auth()
    auth.accessToken(token)
    headers = auth.getHeaders()
    data = jsonable_encoder(category)
    response = requests.post(f"http://product_service:8000/api/v1.0/categorys" , headers=headers ,  json=data   )
    return response.json()


@router.put("/category/update/{id}")
def update_category(id:int  , category:CategoryCreate):

    data = jsonable_encoder(category)
    response = requests.put(f"http://product_service:8000/api/v1.0/categorys/{id}" , json=data   )
    return response.json()

@router.delete("/category/delete/{id}")
def delete_category(id:int ):
    response = requests.delete(f"http://product_service:8000/api/v1.0/categorys/{id}")
    return response.json()

@router.get("/")
def get_all_gateways(authorization: str = Header(None)):
    headers = {}
    if authorization:
        headers["Authorization"] = f"Bearer {authorization}"
    # Make authenticated request using the access token
    response = requests.get("http://product_service:8000/api/v1.0/categorys/?skip=0&limit=100", headers=headers)
    return response.json()


@router.get("/products")
async def getProducts(skip: int = 0, limit: int = 100):
        ob = ProductService()
        response = ob.getProducts(skip , limit)
        return response


# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
@router.get("/user/info")
async def get_user_info(token: str =  Header()):
    headers = {}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    # Make authenticated request using the access token
        response = requests.get("http://user_service:8000/api/v1.0/users/info", headers=headers)
        # if response.json() == 'null':
        #     return 66
        return response.json()
    return token
     
