
import requests
from app.auth.auth import Auth
class InventoryService:
    def __init__(self) -> None:
        self.baseUrl = "http://inventory_service:8000"
        # /api/v1.0/inventorys




    def ProductNumInventory(self ,inventoryID , productID):
        # auth = Auth()
        # auth.accessToken(token)
        # headers = auth.getHeaders()
    
        response = requests.get(self.baseUrl+f"/api/v1.0/inventorys/numbers/{inventoryID}/{productID}")
   
        return response
        
