
from typing import List, Union , Optional
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from pydantic import BaseModel , EmailStr ,  Field




class GovernorateCreate(BaseModel):
    title:str
    en_title:str
    code_government:str

    class Config:
        orm_mode = True


class Governorate(GovernorateCreate):
    id: int 



    class Config:
        orm_mode = True
