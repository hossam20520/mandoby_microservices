
from typing import List, Union , Optional
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from pydantic import BaseModel , EmailStr ,  Field




class Price_list_itemCreate(BaseModel):
    price_list_id:int
    product_id:int
    new_price:float
    discount:float

 
    class Config:
        orm_mode = True


class Price_list_item(Price_list_itemCreate):
    id: int 

    class Config:
        orm_mode = True