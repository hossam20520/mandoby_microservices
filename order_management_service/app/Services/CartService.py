import requests 
from app.avaregions import crud
from app.auth.auth import Auth
class CartService:
    def __init__(self , db , token):
         self.db = db
         self.baseUrl = "http://product_service:8000"
         auth = Auth()
         auth.setCustomToken("token" , token)
         self.headers = auth.getHeaders()
         self.user = auth.getUserInfo()
    

    def GetCartData(self ):
         response = requests.get(self.baseUrl+f"/api/v1.0/carts" , headers=self.headers)
         return response.json()
         