
from sqlalchemy.orm import Session
from app.products.models import ProductModel
from app.products.schemas import ProductCreate , Product
from fastapi import Depends, HTTPException
from sqlalchemy.ext.declarative import DeclarativeMeta as Model
from sqlalchemy.exc import IntegrityError
from app.categorys.models import CategoryModel
from app.global_schemas import ResponseModel
from sqlalchemy.orm import joinedload
from app.units.models import UnitModel
from app.brands.models import BrandModel
from fastapi.encoders import jsonable_encoder


def get_product_pagentation(db: Session, skip: int = 0, limit: int = 100):
        data = db.query(ProductModel).order_by(ProductModel.id.desc())
        items = data.offset(skip).limit(limit).all()
        return {"items":items , "total":data.count()}


def getProducts(db: Session , skip , limit):
         q = (db.query(  ProductModel , CategoryModel, UnitModel  , BrandModel)
         .join(CategoryModel , CategoryModel.id == ProductModel.category_id)
         .join(UnitModel , UnitModel.id == ProductModel.unit_id)
         .join(BrandModel , BrandModel.id == ProductModel.brand_id)
         .order_by(ProductModel.id.desc())
         .offset(skip)
         .limit(limit)
         .all()
         )
         count = (
           db.query(  ProductModel , CategoryModel, UnitModel )
         .join(CategoryModel , CategoryModel.id == ProductModel.category_id)
         .join(UnitModel , UnitModel.id == ProductModel.unit_id).count()
        )


         return {"items":q  , "total":count }
  


def get_product_pagentation_category(db: Session, skip , limit  , category_idd ):
        q = ( db.query(ProductModel, CategoryModel ,  UnitModel )
        .join(CategoryModel, CategoryModel.id == ProductModel.category_id)
        .join(UnitModel , UnitModel.id == ProductModel.unit_id)
        .filter(CategoryModel.id ==  category_idd)
        .order_by(ProductModel.id.desc())
        .offset(skip)  # skip the first 10 results
        .limit(limit)  # return a maximum of 20 results
        .all()
        )

        count = (
        db.query(ProductModel)
        .join(CategoryModel, CategoryModel.id == ProductModel.category_id)
        .filter(CategoryModel.id == category_idd)
        .count()
        )


        return {"items":q  , "total":count }



def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(ProductModel).offset(skip).limit(limit).all()


def get_all_products(db: Session ):
    return db.query(ProductModel).order_by(ProductModel.id.desc()).all()

def create_product(db: Session, product:Product):
    try:
        db_product  = ProductModel(**product.dict())
        db.add(db_product)
        db.commit()
        db.refresh(db_product)
    except IntegrityError:
         db.rollback()
         raise HTTPException(422, ResponseModel([] , "Product already exist" , False , 422 , {"error":"Already exists"})) from None
    return db_product


def delete_all_product(db: Session):
    db.query(ProductModel).delete()
    db.commit()
    return []


def get_product(db: Session, product_id: int):
    return db.query(ProductModel , UnitModel , CategoryModel , BrandModel).join(UnitModel , UnitModel.id == ProductModel.unit_id).join(CategoryModel, CategoryModel.id == ProductModel.category_id).join(BrandModel, BrandModel.id == ProductModel.brand_id).filter(ProductModel.id == product_id).first()


def get_product_by_email(db: Session, email: str):
    return db.query(ProductModel).filter(ProductModel.email == email).first()

def update_product(db: Session , product: dict , id: int):
   db.query(ProductModel).filter(ProductModel.id == id).update(dict(product), synchronize_session = False)
   db.commit()
   return product


def delete_product(db: Session , id:int):
    db_model = db.query(ProductModel).get(id)
    if db_model:
         db.delete(db_model)
         db.commit() 
         return db_model
            
    else:
          raise HTTPException(status_code=404, detail=ResponseModel([] , "Product not found" , True , 404 , {}))
