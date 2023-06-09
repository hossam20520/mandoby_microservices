from typing import List, Union , Optional
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from pydantic import BaseModel , EmailStr ,  Field




class UserCreate(BaseModel):
    first_name:str 
    last_name:str 
    username:str 
    email:str
    phone:str
    hashed_password:str 
    is_active:bool

    class Config:
        orm_mode = True


class User(UserCreate):
    id: int 

    class Config:
        orm_mode = True




class UserData(BaseModel):
    name:str 
    first_name:str 
    last_name:str 
    username:str 
    email:str
    phone:str
    is_active:bool
    roles:list
    permissions:list

    class Config:
        orm_mode = True


class UserInfo(UserData):
    id: int 

    class Config:
        orm_mode = True