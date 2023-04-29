
from typing import List, Union , Optional
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from pydantic import BaseModel , EmailStr ,  Field




class cartPayload(BaseModel):
    product_id:int
    qty:int


    class Config:
        orm_mode = True



class Items(BaseModel):
      cart_id:int
      product_id:int
      quantity:int 
      price:float
      subtotal:float





class CartCreate(BaseModel):
    total:float
    discount:float 
    user_id:int
    order_id:int


    class Config:
        orm_mode = True


class Cart(CartCreate):
    id: int 

    class Config:
        orm_mode = True