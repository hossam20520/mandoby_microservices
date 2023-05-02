
from typing import List , Annotated
from fastapi import APIRouter, Body , Header
from fastapi import Depends, FastAPI, HTTPException , Form  , UploadFile , File
from sqlalchemy.orm import Session
# from app.database import SessionLocal, engine
from fastapi.security import HTTPBearer, HTTPBasicCredentials
import requests
from app.auth.auth import Auth
from fastapi.encoders import jsonable_encoder
from app.services.GovernmentService import GovernmentService
# from app.users_gateway.schemas import UserCreate
router = APIRouter()



@router.get("/list/")
def gove_list( skip: int = 0, limit: int = 100 , token: str =  Header()):
    auth = Auth()
    auth.accessToken(token)
    headers = auth.getHeaders()
    # Communicate to region 
    regi = GovernmentService()
    respone = regi.getGovs(skip , limit)
    return respone








