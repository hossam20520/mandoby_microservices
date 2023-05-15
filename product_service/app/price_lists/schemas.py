
from typing import List, Union , Optional
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from pydantic import BaseModel , EmailStr ,  Field




class Price_listCreate(BaseModel):
    en_title:str
    ar_title:str
    is_active:bool
    


    class Config:
        orm_mode = True


class Price_list(Price_listCreate):
    id: int 

    class Config:
        orm_mode = True