
from typing import List, Union , Optional
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from pydantic import BaseModel , EmailStr ,  Field




class AddresseCreate(BaseModel):
    user_id:int
    lat:str
    long:str
    name:str 
    address:str
    govern_id:int
    govern_name:str
    region:str
    region_id:int
    mobile:str
    notes:str
    selected:bool
    deleted:bool


    class Config:
        orm_mode = True


class Addresse(AddresseCreate):
    id: int 

    class Config:
        orm_mode = True