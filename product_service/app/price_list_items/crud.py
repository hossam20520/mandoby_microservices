
from sqlalchemy.orm import Session
from app.price_list_items.models import Price_list_itemModel
from app.price_lists.models import Price_listModel
from app.products.models import ProductModel
from app.price_list_items.schemas import Price_list_itemCreate , Price_list_item
from app.categorys.models import CategoryModel
from fastapi import Depends, HTTPException
from sqlalchemy.ext.declarative import DeclarativeMeta as Model
from sqlalchemy.exc import IntegrityError
from app.global_schemas import ResponseModel



def get_price_list_items_one(db: Session,skip , limit  ,  price_list_item_id ):
    q = (db.query(Price_list_itemModel , ProductModel  , Price_listModel  )
    .join(Price_list_itemModel , Price_list_itemModel.price_list_id == Price_listModel.id)
    .join(ProductModel , ProductModel.id == Price_list_itemModel.product_id).filter(Price_list_itemModel.price_list_id == price_list_item_id)
     .order_by(Price_list_itemModel.id.desc())
    .offset(skip)
    .limit(limit)
    .all()
    ) 
    count = (
    db.query( Price_list_itemModel , ProductModel  , Price_listModel )
    .join(Price_list_itemModel , Price_list_itemModel.price_list_id == Price_listModel.id)
    .join(ProductModel , ProductModel.id == Price_list_itemModel.product_id).filter(Price_list_itemModel.price_list_id == price_list_item_id).count()
    )

    return  {"items":q  , "total":count }

def get_price_list_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Price_list_itemModel).offset(skip).limit(limit).all()

def create_price_list_item(db: Session, price_list_item:Price_list_item):

    db_model = db.query(Price_list_itemModel).filter(Price_list_itemModel.product_id == price_list_item.product_id).filter(Price_list_itemModel.price_list_id == price_list_item.price_list_id).first()
    if db_model:
         raise HTTPException(status_code=404, detail=ResponseModel([] , "Price_list_item not found" , True , 404 , {}))   
    else:
        try:
            db_price_list_item  = Price_list_itemModel(**price_list_item.dict())
            db.add(db_price_list_item)
            db.commit()
            db.refresh(db_price_list_item)
        except IntegrityError:
            db.rollback()
            raise HTTPException(422, ResponseModel([] , "Price_list_item already exist" , False , 422 , {"error":"Already exists"})) from None
        return db_price_list_item


def delete_all_price_list_item(db: Session):
    db.query(Price_list_itemModel).delete()
    db.commit()
    return []


def get_price_list_item(db: Session, price_list_item_id: int):
    return db.query(Price_list_itemModel).filter(Price_list_itemModel.id == price_list_item_id).first()


def get_price_list_item_by_email(db: Session, email: str):
    return db.query(Price_list_itemModel).filter(Price_list_itemModel.email == email).first()

def update_price_list_item(db: Session , price_list_item: dict , id: int):
   db.query(Price_list_itemModel).filter(Price_list_itemModel.id == id).update(dict(price_list_item), synchronize_session = False)
   db.commit()
   return price_list_item


def delete_price_list_item(db: Session , id:int):
    db_model = db.query(Price_list_itemModel).get(id)
    if db_model:
         db.delete(db_model)
         db.commit() 
         return db_model
            
    else:
          raise HTTPException(status_code=404, detail=ResponseModel([] , "Price_list_item not found" , True , 404 , {}))
