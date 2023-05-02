
from typing import List, Union , Optional
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from pydantic import BaseModel , EmailStr ,  Field




class AvagovCreate(BaseModel):
    ar_title:str
    en_title:str
    code:str
    lat:str
    long:str
    ava:bool
    deleted:bool



    class Config:
        orm_mode = True


class Avagov(AvagovCreate):
    id: int 

    class Config:
        orm_mode = True