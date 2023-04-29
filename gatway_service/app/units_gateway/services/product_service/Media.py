import requests

class Media:
    def __init__(self) -> None:
        pass



    def CategoryImage(self , name):
        response = requests.get(f"http://product_service:8000/api/v1.0/categorys/get/image?name={name}")
        return response
