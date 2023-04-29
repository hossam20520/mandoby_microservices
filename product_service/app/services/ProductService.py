
import requests
from app.auth.auth import Auth
class ProductService:
    def __init__(self) -> None:
        self.baseUrl = "http://product_service:8000"
        # /api/v1.0/inventorys




    def getProductInfo(self , productID):
        # auth = Auth()
        # auth.accessToken(token)
        # headers = auth.getHeaders()
        
        response = requests.get(self.baseUrl+f"/api/v1.0/products/{productID}")
        return response
        
