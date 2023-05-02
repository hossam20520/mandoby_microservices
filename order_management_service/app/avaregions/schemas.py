
from typing import List, Union , Optional
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from pydantic import BaseModel , EmailStr ,  Field




class AvaregionCreate(BaseModel):
    gov_id:int
    ar_title:str
    en_title:str
    code:str
    lat:str
    long:str
    ava:bool
    deleted:bool


    class Config:
        orm_mode = True


class Avaregion(AvaregionCreate):
    id: int 

    class Config:
        orm_mode = True