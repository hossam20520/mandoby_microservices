
from typing import List , Annotated
from fastapi import APIRouter, Body , Header
from fastapi import Depends, FastAPI, HTTPException , Form  , UploadFile , File
from sqlalchemy.orm import Session
# from app.database import SessionLocal, engine
from fastapi.security import HTTPBearer, HTTPBasicCredentials
import requests
from app.auth.auth import Auth
from app.cart_gateway.schemas import cartPayload  
from fastapi.encoders import jsonable_encoder
from app.services.InventoryService import InventoryService
router = APIRouter()





@router.get("/mycart")
def addToCart(   token: str =  Header()):
    auth = Auth()
    auth.setCustomToken("token" , token)
    headers = auth.getHeaders()
    response = requests.get(f"http://product_service:8000/api/v1.0/carts" ,  headers=headers  )
    return response.json()



@router.post("/")
def addToCart( cart:cartPayload , token: str =  Header()):
    auth = Auth()
    # auth.accessToken(token)
    auth.setCustomToken("token" , token)
    headers = auth.getHeaders()
    data = jsonable_encoder(cart)
    response = requests.post(f"http://product_service:8000/api/v1.0/carts" ,  headers=headers  , json=data  )
    return response.json()




@router.delete("/delete/{productId}")
def addToCart( productId:int  , token: str =  Header()):
    auth = Auth()
    auth.setCustomToken("token" , token)
    headers = auth.getHeaders()
    response = requests.delete(f"http://product_service:8000/api/v1.0/carts/{productId}" ,   headers=headers    )
    return response.json()


# @router.post("/create")
# def create_user( unit:UnitCreate ,  token: str =  Header()):
#     auth = Auth()
#     auth.accessToken(token)
#     headers = auth.getHeaders()
#     data = jsonable_encoder(unit)
#     response = requests.post(f"http://product_service:8000/api/v1.0/units" ,   headers=headers  , json=data   )
#     return response.json()



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






