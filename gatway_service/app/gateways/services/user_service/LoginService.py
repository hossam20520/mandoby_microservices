import requests

class LoginService:

    def __init__(self) -> None:
        pass


    def ClientLogin(self, phone , password):
        data = {
                "username": phone,
                "password": password
                }
        response = requests.post("http://user_service:8000/api/v1.0/login/phone" , json=data)
        
        return response.json()
