
from typing import List, Union , Optional
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from pydantic import BaseModel , EmailStr ,  Field




class Order_managementCreate(BaseModel):
    title:str

    class Config:
        orm_mode = True


class Order_management(Order_managementCreate):
    id: int 

    class Config:
        orm_mode = True