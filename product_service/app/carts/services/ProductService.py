
import requests
from app.auth.auth import Auth
class ProductService:
    def __init__(self) -> None:
        self.baseUrl = "http://product_service:8000"
        # 



    def getProductInfo(self , id , token ):
        auth = Auth()
        auth.accessToken(token)
        headers = auth.getHeaders()
        response = requests.get(self.baseURL+f"/api/v1.0/products/{id}" ,  headers=headers  )
        return response.json()
