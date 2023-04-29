
from typing import List , Annotated
from fastapi import APIRouter, Body , Header
from fastapi import Depends, FastAPI, HTTPException , Form  , UploadFile , File
from sqlalchemy.orm import Session
# from app.database import SessionLocal, engine
from fastapi.security import HTTPBearer, HTTPBasicCredentials
import requests
from app.auth.auth import Auth
from fastapi.encoders import jsonable_encoder
from app.products_gateway.schemas import ProductCreate
router = APIRouter()








@router.get("/list")
def product_list(skip: int = 0, limit: int = 100 , token: str =  Header()):
    auth = Auth()
    auth.accessToken(token)
    headers = auth.getHeaders()
    response = requests.get(f"http://product_service:8000/api/v1.0/products/pagentation" , headers=headers   )
    return response.json()



@router.get("/moble/list")
def product_list(skip: int = 0, limit: int = 100 , token: str =  Header()):
    auth = Auth()
    auth.accessToken(token)
    headers = auth.getHeaders()
    response = requests.get(f"http://product_service:8000/api/v1.0/products/mobile/pagentation?skip={skip}&limit={limit}" , headers=headers   )
    return response.json()


@router.post("/create")
def create_user( product:ProductCreate ,  token: str =  Header()):
    auth = Auth()
    auth.accessToken(token)
    headers = auth.getHeaders()
    data = jsonable_encoder(product)
    response = requests.post(f"http://product_service:8000/api/v1.0/products" ,   headers=headers  , json=data   )
    return response.json()



# @router.put("/update/{id}")
# def update_user(id:int  , user:UserCreate ,  token: str =  Header()):
#     auth = Auth()
#     auth.accessToken(token)
#     headers = auth.getHeaders()
#     data = jsonable_encoder(user)
#     response = requests.put(f"http://user_service:8000/api/v1.0/users/{id}" ,   headers=headers  , json=data   )
#     return response.json()




# @router.delete("/delete/{id}")
# def delete_user(id:int  ,  token: str =  Header()):
#     auth = Auth()
#     auth.accessToken(token)
#     headers = auth.getHeaders()
#     response = requests.delete(f"http://user_service:8000/api/v1.0/users/{id}" ,   headers=headers   )
#     return response.json()






