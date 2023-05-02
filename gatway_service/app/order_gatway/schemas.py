
from typing import List, Union , Optional
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from pydantic import BaseModel , EmailStr ,  Field
from datetime import datetime



class OrderCreate(BaseModel):
    order_number:str
    user_id:int
    address_id:int
    person_delevery_id:int
    order_date: Optional[datetime] = None
    shop_id:int
    payment_id:int
    shipping_id:int
    cart_id:int
    tax:float
    shipping_price:float
    discount:float
    other_discount:float
    subtotal:float
    total:float

    class Config:
        orm_mode = True


class Order(OrderCreate):
    id: int 

    class Config:
        orm_mode = True