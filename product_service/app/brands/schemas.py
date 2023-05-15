
from typing import List, Union , Optional
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from pydantic import BaseModel , EmailStr ,  Field




class BrandCreate(BaseModel):
    en_title:str
    ar_title:str
    description:str 
    image:str 


    class Config:
        orm_mode = True
 
class Brand(BrandCreate):
    id: int 

    class Config:
        orm_mode = True