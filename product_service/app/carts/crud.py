
from sqlalchemy.orm import Session
from app.carts.models import CartModel , CartItemModel
from app.carts.schemas import CartCreate , Cart , Items
from fastapi import Depends, HTTPException
from sqlalchemy.ext.declarative import DeclarativeMeta as Model
from sqlalchemy.exc import IntegrityError
from app.global_schemas import ResponseModel
from sqlalchemy.orm import joinedload
from app.products.models import ProductModel
from sqlalchemy import desc




def deleteItemFromCart(db:Session , productID , cartID):
    db_model = db.query(CartItemModel).filter(CartItemModel.cart_id == cartID ,CartItemModel.product_id == productID ).first()
    if db_model:
         db.delete(db_model)
         db.commit() 
         return db_model
            
    else:
          raise HTTPException(status_code=404, detail=ResponseModel([] , "Item not found" , True , 404 , {}))


def getCartItems(db: Session , cart_id):
    cart = db.query(CartModel).filter_by(id=cart_id).first()
    if cart is None:
        return None
    
    cart_items = db.query(CartItemModel, ProductModel).\
        filter(CartItemModel.cart_id == cart.id).\
        filter(CartItemModel.product_id == ProductModel.id).\
        order_by(desc(CartItemModel.id)).\
        all()

    cart_items_data = []
    for cart_item, product in cart_items:
        cart_item_data = {
            'id': cart_item.id,
            'cart_id': cart_item.cart_id,
            'product_id': cart_item.product_id,
            'quantity': cart_item.quantity,
            'price': cart_item.price,
            'subtotal': cart_item.subtotal,
            'product': {
                'id': product.id,
                'name': product.ar_title,
                'price': product.price,
                'image': product.image,
                # 'description': product.description,
                # add any other product fields you need
            }
        }
        cart_items_data.append(cart_item_data)

    cart_data = {
        'id': cart.id,
        'total': cart.total,
        'discount': cart.discount,
        'user_id': cart.user_id,
        'order_id': cart.order_id,
        'items': cart_items_data
    }

    return cart_data

def get_carts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(CartModel).offset(skip).limit(limit).all()


def create_cart(db: Session, CartModel:CartModel):
        db_cart  = CartModel
        db.add(db_cart)
        db.commit()
        db.refresh(db_cart)
        return db_cart


def create_cart_item(db: Session, CartItemModel:CartItemModel):
        db_cart_item  = CartItemModel
        db.add(db_cart_item)
        db.commit()
        db.refresh(db_cart_item)
        return db_cart_item


def delete_all_cart(db: Session):
    db.query(CartModel).delete()
    db.commit()
    return []


def CartByUserAnOrder(db: Session, userID: int):
     return  db.query(CartModel).filter(CartModel.user_id == userID ,  CartModel.order_id == 0).first()

def SelectItemBy(db: Session, productID: int , cartID:int):
     return  db.query(CartItemModel).filter(CartItemModel.product_id == productID ,  CartItemModel.cart_id == cartID).first()


def GetCartItem(db: Session, cartID: int , UserID):
    cart_items = db.query(CartItemModel).\
                    filter(CartItemModel.cart_id == cartID).\
                    filter(CartModel.user_id == UserID).\
                    all()
    return  cart_items

# If cart is not None, then a matching CartModel object was found in the database

def updateItemQuantity(db: Session, prductID: int ,  cartID:int , cartItem:dict):
   db.query(CartItemModel).filter(CartItemModel.product_id == prductID , CartItemModel.cart_id == cartID).update(dict(cartItem), synchronize_session = False)
   db.commit()
   return cartItem

def get_cart(db: Session, cart_id: int):
    return db.query(CartModel).filter(CartModel.id == cart_id).first()


def get_cart_by_email(db: Session, email: str):
    return db.query(CartModel).filter(CartModel.email == email).first()

def update_cart(db: Session , cart: dict , id: int):
   db.query(CartModel).filter(CartModel.id == id).update(dict(cart), synchronize_session = False)
   db.commit()
   return cart


def delete_cart(db: Session , id:int):
    db_model = db.query(CartModel).get(id)
    if db_model:
         db.delete(db_model)
         db.commit() 
         return db_model
            
    else:
          raise HTTPException(status_code=404, detail=ResponseModel([] , "Cart not found" , True , 404 , {}))
