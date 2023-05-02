import requests 
from app.auth.auth import Auth

class AdressesService:
    def __init__(self , token):
         self.baseURL = "http://order_management_service:8000"
         auth = Auth()
         #    auth.accessToken(token)
         auth.setCustomToken("token", token)
         self.headers = auth.getHeaders()
    def createAddress(self  , data):
         

         response = requests.post(self.baseURL+f"/api/v1.0/addresses" , json=data )
         return response.json()
     #     return crud.get_avaregion_by_gove(self.db , skip , limit , goveID)


    
    def GetMyaddresses(self):
        response = requests.get(self.baseURL+"/api/v1.0/addresses/my/addresses" ,  headers=self.headers )
        return response.json()
    
    def updateAddresses(self ):
        response = requests.put(self.baseURL+"/api/v1.0/addresses/" , headers=self.headers )
        return response.json()
         