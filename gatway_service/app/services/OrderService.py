import requests 
from app.auth.auth import Auth

class OrderService:
    def __init__(self , token):
         self.baseURL = "http://order_management_service:8000"
         auth = Auth()
         auth.setCustomToken("token", token)
         self.headers = auth.getHeaders()
         
    def CreateOrder(self ,  data ):
         response = requests.get(self.baseURL+f"/api/v1.0/orders/create" , json=data  , headers=self.headers )
         return response.json()
     #     return crud.get_avaregion_by_gove(self.db , skip , limit , goveID)
         