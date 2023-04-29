from typing import List, Union , Optional
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String 
from pydantic import BaseModel , EmailStr ,  Field




class ProductCreate(BaseModel):
    en_title:str
    ar_title:str 
    desc:str
    discount:float
    slug:str 
    code:str
    Type_barcode:str 
    price:float 
    cost:float 
    category_id:int 
    unit_id:int 
    unit_sale_id:int 
    unit_purchase_id:int
    TaxNet:float
    tax_method:str 
    image:str
    note:str 
    stock_alert:float
    is_variant:bool 
    is_active:bool


    class Config:
        orm_mode = True


class Product(ProductCreate):
    id: int 


    class Config:
        orm_mode = True