
from typing import List
from fastapi import APIRouter, Body , Header
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import app.carts.models as models 
from app.carts.models import CartModel , CartItemModel
import app.carts.crud as crud 
from app.carts.schemas import cartPayload , Cart , CartCreate , Items 
from app.database import SessionLocal, engine
from app.global_schemas import ResponseModel , ResponseModelSchema
from app.carts.controller.cart import Cart
from fastapi.encoders import jsonable_encoder
from app.auth.auth import Auth
from app.services.InventoryService import InventoryService
from app.services.ProductService import ProductService
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



router = APIRouter()

# @router.get("/")
# def addTocart(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     # carts = crud.get_carts(db, skip=skip, limit=limit)
#     cart = Cart()
#     da = cart.CreateCart()
#     json = jsonable_encoder(da)
    
#     return json



# @router.get("/addcart")
# def add_carts(  db: Session = Depends(get_db)):
#     carts = crud.get_carts(db, )
#     return carts


@router.get("/")
def Get_cart_data(db: Session = Depends(get_db) , token: str = Header() ):
     auth = Auth()
     auth.accessToken(token)
     user = auth.getUserInfo()
     cart = crud.CartByUserAnOrder(db , user['id']) 
     if cart == None:
         return []
     items = crud.getCartItems(db , cart.id)
     if items == None:
         return []
     return items


@router.delete("/{productID}")
def DeleteItemFromCart( productID:int , db: Session = Depends(get_db) , token: str = Header() ):
        auth = Auth()
        auth.accessToken(token)
        user = auth.getUserInfo()
        cart = crud.CartByUserAnOrder(db , user['id']) 
        cartID  = cart.id
        deletedData = crud.deleteItemFromCart(db , productID  , cartID )


        newTotal =   cart.total - deletedData.subtotal
        updatedcart = CartModel(user_id=user['id'] , total= newTotal)
        crud.update_cart(db , jsonable_encoder(updatedcart) ,cartID)
        return "success"




@router.post("/")
def create_cart(data: cartPayload, db: Session = Depends(get_db)  , token: str = Header() ):
    auth = Auth()
    auth.accessToken(token)
    user = auth.getUserInfo()

    # 1 - Inventory Service
    invent = InventoryService()
    stock = invent.ProductNumInventory(1, data.product_id)
    if stock.status_code == 404:
       return stock.json()
    
    stock = stock.json()
    if( data.qty >   stock['qty']):
        raise HTTPException(status_code=404, detail=ResponseModel([] , "No enough products" , False , 409 , {}))  
    # End Inventory Service    


    # 2 -communcate to product service to get product info like price and discount before calclute cart  total
    product = ProductService()
    productInfo = product.getProductInfo(data.product_id)
    if productInfo.status_code == 404:
        return productInfo.json()
    
    productInfo = productInfo.json()
    
    if(data.qty == 0 ):
        data.qty =1
    # TODO add Decription to product  Done
    # TODO Add discount for prodduct here and add this line   ( data.qty * (productInfo['price'] - productInfo['discount']  ),
    # TODO Add Discount copuns here and add it to Discount 
    # TODO Add total field to cart Item  and add this line to cartItem  ( "total": ( productInfo['price'] - productInfo['discount']) * data.qty )
    # totalCartPrice =  data.qty *  productInfo['price']

    originalPrice = productInfo['product']['ProductModel']['price']    #add discount here
    qtyStock = stock['qty']
    productId = productInfo['product']['ProductModel']['id']
    userid = user['id']
    demand_qty = data.qty
    cart = crud.CartByUserAnOrder(db , user['id']) 
    total = data.qty * originalPrice


    if cart is not None:
        cart_id = cart.id
        CurrentTotalCart = cart.total
        # return cart items by product id and cart id 
        item = crud.SelectItemBy(db ,productId , cart_id)
        if item is not None:
            # this add max items if the demand qty is larger than the stock 
            if  (item.quantity + demand_qty)  >  qtyStock:
                 demand_qty = qtyStock - item.quantity
   
            # stop decrese when the queantiy is one 
            if item.quantity == 1 and demand_qty == -1:
                return "success"
            cartITem = CartItemModel(quantity = demand_qty + item.quantity  , subtotal = item.subtotal + (originalPrice * demand_qty))
            crud.updateItemQuantity(db , productId , cart_id ,  jsonable_encoder(cartITem) )

            # update cart code
            newTotal =  ( demand_qty * originalPrice ) + CurrentTotalCart
            updatedcart = CartModel(user_id=userid , total= newTotal)
            crud.update_cart(db , jsonable_encoder(updatedcart) ,cart_id)
            # end update cart

            return "success"
        else: 
           cartItemModel = CartItemModel(cart_id = cart_id , product_id =productId , quantity = demand_qty , price = originalPrice , subtotal = demand_qty * originalPrice )
           crud.create_cart_item(db , cartItemModel )
         
           # update cart
           newTotal =  ( demand_qty  * originalPrice ) + CurrentTotalCart
           updatedcart = CartModel(user_id=userid , total= newTotal)
           crud.update_cart(db , jsonable_encoder(updatedcart) ,cart_id)
           # end update cart code

           return "success"

    else:
    #    Once only
       cart = CartModel(user_id=userid , total= total)
       cartD = crud.create_cart(db ,cart ) 
      
       cartItemModel = CartItemModel(cart_id = cartD.id , product_id =productId , quantity = data.qty , price = originalPrice , subtotal = data.qty * originalPrice )
       crud.create_cart_item(db , cartItemModel )
       return "success"


