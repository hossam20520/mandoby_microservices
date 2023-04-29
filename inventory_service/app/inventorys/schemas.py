
from typing import List, Union , Optional
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from pydantic import BaseModel , EmailStr ,  Field




class InventoryCreate(BaseModel):
    name:str
    statut:bool
    image:str
    class Config:
        orm_mode = True


class Inventory(InventoryCreate):
    id: int 

    class Config:
        orm_mode = True