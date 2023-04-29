import requests

class Auth:
    def __init__(self) -> None:
        self.headers = {}


    def getHeaders(self):
           return self.headers
        

    def accessToken(self , token):
         if token:
             self.headers["Authorization"] = f"Bearer {token}"


    def setCustomToken(self , name ,  token):
         if token:
              self.headers[name] = f"{token}"

    def getUserInfo(self):
        response = requests.get("http://user_service:8000/api/v1.0/users/info", headers=self.headers)
        return response.json()
     