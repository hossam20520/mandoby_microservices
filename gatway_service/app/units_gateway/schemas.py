
from typing import List, Union , Optional
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from pydantic import BaseModel , EmailStr ,  Field




class UnitCreate(BaseModel):
    en_title:str
    ar_title:str
    ShortName:str
    base_unit:int
    operator:str
    operator_value:float



    class Config:
        orm_mode = True


class Unit(UnitCreate):
    id: int 

    class Config:
        orm_mode = True