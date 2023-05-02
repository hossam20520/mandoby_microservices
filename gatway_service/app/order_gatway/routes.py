
from typing import List , Annotated
from fastapi import APIRouter, Body , Header
from fastapi import Depends, FastAPI, HTTPException , Form  , UploadFile , File
from sqlalchemy.orm import Session
# from app.database import SessionLocal, engine
from fastapi.security import HTTPBearer, HTTPBasicCredentials
import requests
from app.auth.auth import Auth
from fastapi.encoders import jsonable_encoder
from app.services.OrderService import OrderService
from app.order_gatway.schemas import OrderCreate
# from app.users_gateway.schemas import UserCreate
router = APIRouter()



@router.post("/create")
def regions_list( data:OrderCreate , token: str =  Header()):

    # Communicate to order services 
    order = OrderService(token)
    data = jsonable_encoder(data)
    respone = order.CreateOrder(data)
    return respone








