from app.carts.crud import create_cart
from app.carts.models import CartModel
from app.carts.schemas import  CartCreate
from app.carts import crud
from app.carts.schemas import Items
from app.carts.schemas import cartPayload 


class Cart:
    def __init__(self , db ):
        self.db  = db
        self.cartID = 0
        self.product = {}
        self.user = {}
        self.inventoryID = 1
        self.payload:cartPayload
        # self.cartItem:Items = {
        # "cart_id":0,
        # "product_id": self.product['id'],
        # "quantity":self.payload.qty,
        # "price":0
        #    }
      
    def addPyload(self, payload:cartPayload):
        self.payload = payload

    def setInventory(self, invID):
        self.inventoryID = invID

  
    def cartIItemObj(self , cartID = 0 , productID = 0 , qty = 0, price =0 ):
        pass 
    
    def AddProduct(self , product):
        self.product = product

    def AddUser(self, user):
        self.user = user
     
    
    def getCartByID(self):
        pass

    def  HaveCart(self):
         return self.user
        #  cart = crud.CartByUserAnOrder(self.db , user['id']) 
        #  if cart is not None:
        #      return True

    
    # def add(self):
    #     return self.cartItem

    # def AddItems(self ,   user , prdouct ):
 
    #       item = {
    #            "cart_id":0,
    #            "product_id":0,
    #            "quantity":5,
    #            "price":50 
    #              }
    #       return create_cart_item(self.db ,item )




    # def Create(self):
    #     pass
    # # def CreateCart(self ):
    # #     #  CartCreate 
  
    # #     return CartModel
     
    # #     # create_cart(user)
    
 