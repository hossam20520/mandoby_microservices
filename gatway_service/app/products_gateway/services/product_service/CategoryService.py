import requests


class CategoryService:
    def __init__(self) -> None:
        pass

    def Category(self , skip , limit):
        response = requests.get(f"http://product_service:8000/api/v1.0/categorys/?skip={skip}&limit={limit}")
        return response.json()