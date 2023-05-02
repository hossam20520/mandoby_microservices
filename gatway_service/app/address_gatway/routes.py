
from typing import List , Annotated
from fastapi import APIRouter, Body , Header
from fastapi import Depends, FastAPI, HTTPException , Form  , UploadFile , File
from sqlalchemy.orm import Session
# from app.database import SessionLocal, engine
from fastapi.security import HTTPBearer, HTTPBasicCredentials
import requests
from app.auth.auth import Auth
from fastapi.encoders import jsonable_encoder
from app.services.AdressesService import AdressesService 
from app.address_gatway.schemas import AddresseCreate , AddresseCreateUser
# from app.users_gateway.schemas import UserCreate
router = APIRouter()



@router.post("/")
def address_create(  data:AddresseCreateUser , token: str =  Header()):
    auth = Auth()
    auth.accessToken(token)
    user = auth.getUserInfo()
    # Communicate to region 
    
  
    address = AdressesService(token)

    respone = address.updateAddresses()
    data:AddresseCreate = {
            "user_id":  user['id'],
            "lat": "string",
            "long": "string",
            "name": "string",
            "address": data.address,
            "govern_id": data.govern_id,
            "govern_name": "string",
            "region": "string",
            "region_id": data.region_id,
            "mobile": data.mobile,
            "notes": data.notes,
            "selected": True,
            "deleted": False
            }
    


    # data = jsonable_encoder(data)
     
    respone = address.createAddress(data)
    return respone


@router.get("/myaddress")
def GetAddressByUser(token: str =  Header()):
    address = AdressesService(token)
    data = address.GetMyaddresses()
    return data

#  'http://localhost:8080/api/v1.0/addresses/my/addresses?user=1'

