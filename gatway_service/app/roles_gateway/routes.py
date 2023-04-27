
from typing import List , Annotated
from fastapi import APIRouter, Body , Header
from fastapi import Depends, FastAPI, HTTPException , Form  , UploadFile , File
from sqlalchemy.orm import Session
# from app.database import SessionLocal, engine
from fastapi.security import HTTPBearer, HTTPBasicCredentials
import requests
from app.auth.auth import Auth
from fastapi.encoders import jsonable_encoder
from app.roles_gateway.schemas import RoleCreate
# from app.users_gateway.schemas import UserCreate
router = APIRouter()



@router.get("/list")
def roles_list(skip: int = 0, limit: int = 100 , token: str =  Header()):
    auth = Auth()
    auth.accessToken(token)
    headers = auth.getHeaders()
    response = requests.get(f"http://user_service:8000/api/v1.0/roles/pagentaion" , headers=headers   )
    return response.json()




@router.post("/create")
def role_user(role: RoleCreate ,  token: str =  Header()):
    auth = Auth()
    auth.accessToken(token)
    headers = auth.getHeaders()
    data = jsonable_encoder(role)
    response = requests.post(f"http://user_service:8000/api/v1.0/roles" ,   headers=headers  , json=data   )
    return response.json()



@router.put("/update/{id}")
def update_role(id:int  ,role: RoleCreate ,  token: str =  Header()):
    auth = Auth()
    auth.accessToken(token)
    headers = auth.getHeaders()
    data = jsonable_encoder(role)
    response = requests.put(f"http://user_service:8000/api/v1.0/roles/{id}" ,   headers=headers  , json=data   )
    return response.json()




@router.delete("/delete/{id}")
def delete_role(id:int  ,  token: str =  Header()):
    auth = Auth()
    auth.accessToken(token)
    headers = auth.getHeaders()
    response = requests.delete(f"http://user_service:8000/api/v1.0/roles/{id}" ,   headers=headers   )
    return response.json()






