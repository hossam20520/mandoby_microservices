import requests

class ProductService:
    def __init__(self) -> None:
        pass


    def getProducts(self , skip , limit):
        response = requests.get(f"http://product_service:8000/api/v1.0/products/?skip={skip}&limit={limit}")
        return response.json()