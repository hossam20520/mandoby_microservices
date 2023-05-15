
from typing import List, Union , Optional
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from pydantic import BaseModel , EmailStr ,  Field




class CategoryCreate(BaseModel):
    en_title:str
    ar_title:str
    code:str 
    image:str 
   

    class Config:
        orm_mode = True


class Category(CategoryCreate):
    id: int 

    class Config:
        orm_mode = True


class CategoryUpdate(BaseModel):
    en_title:str =   Field(default=None, description="Optional name")
    ar_title:str =   Field(default=None, description="Optional name")
    code:str  =   Field(default=None, description="Optional name")
    image:str  =   Field(default=None, description="Optional name")


       