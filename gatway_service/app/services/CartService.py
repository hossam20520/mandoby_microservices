import requests
from app.auth.auth import Auth
from fastapi.encoders import jsonable_encoder

class CartService:

    def __init__(self) -> None:
        self.baseURL = "http://product_service:8000/api/v1.0/carts"


    def addTOCart(self, token , product):
        auth = Auth()
        auth.accessToken(token)
        headers = auth.getHeaders()
        user = auth.getUserInfo()
        
        # data = jsonable_encoder(product)
        cartData = {
            ""
        }

        response = requests.post(self.baseURL ,  headers=headers ,  json=data )
        return response.json()