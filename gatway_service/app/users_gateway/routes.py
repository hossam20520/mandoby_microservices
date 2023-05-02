
from typing import List , Annotated
from fastapi import APIRouter, Body , Header
from fastapi import Depends, FastAPI, HTTPException , Form  , UploadFile , File
from sqlalchemy.orm import Session
# from app.database import SessionLocal, engine
from fastapi.security import HTTPBearer, HTTPBasicCredentials
import requests
from app.auth.auth import Auth
from fastapi.encoders import jsonable_encoder
from app.users_gateway.schemas import UserCreate
from app.auth.auth import Auth
router = APIRouter()



@router.get("/list")
def users_list(skip: int = 0, limit: int = 100 , token: str =  Header()):
    auth = Auth()
    auth.accessToken(token)
    headers = auth.getHeaders()
    response = requests.get(f"http://user_service:8000/api/v1.0/users/pagentation" , headers=headers   )
    return response.json()



@router.post("/register")
def create_user( user:UserCreate):

    data = jsonable_encoder(user)
    response = requests.post(f"http://user_service:8000/api/v1.0/register/client" ,  json=data )
    return response.json()



@router.post("/create")
def create_user( user:UserCreate ,  token: str =  Header()):
    auth = Auth()
    auth.accessToken(token)
    headers = auth.getHeaders()
    data = jsonable_encoder(user)
    response = requests.post(f"http://user_service:8000/api/v1.0/register" ,   headers=headers  , json=data   )
    return response.json()



@router.put("/update/{id}")
def update_user(id:int  , user:UserCreate ,  token: str =  Header()):
    auth = Auth()
    auth.accessToken(token)
    headers = auth.getHeaders()
    data = jsonable_encoder(user)
    response = requests.put(f"http://user_service:8000/api/v1.0/users/{id}" ,   headers=headers  , json=data   )
    return response.json()




@router.delete("/delete/{id}")
def delete_user(id:int  ,  token: str =  Header()):
    auth = Auth()
    auth.accessToken(token)
    headers = auth.getHeaders()
    response = requests.delete(f"http://user_service:8000/api/v1.0/users/{id}" ,   headers=headers   )
    return response.json()


@router.get("/user/info")
async def get_user_info(token: str =  Header()):
    auth = Auth()
    auth.accessToken(token)
    user = auth.getUserInfo()
    return user



