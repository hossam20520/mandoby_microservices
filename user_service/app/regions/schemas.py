
from typing import List, Union , Optional
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from pydantic import BaseModel , EmailStr ,  Field




class RegionCreate(BaseModel):
    title:str
    en_title:str
    code_region:str
    gov_id: int

    class Config:
        orm_mode = True


class Region(RegionCreate):
    id: int 

    class Config:
        orm_mode = True