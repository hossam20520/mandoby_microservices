

class Auth:
    def __init__(self) -> None:
        self.headers = {}


    def getHeaders(self):
           return self.headers
        

    def accessToken(self , token):
         if token:
             self.headers["Authorization"] = f"Bearer {token}"