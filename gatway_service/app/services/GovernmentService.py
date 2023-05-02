import requests 


class GovernmentService:
    def __init__(self):
         self.baseURL = "http://order_management_service:8000"

    def getGovs(self , skip=0 , limit=100  ):
         response = requests.get(self.baseURL+f"/api/v1.0/avagovs/pagentation/?skip={skip}&limit={limit}"  )
         return response.json()
     #     return crud.get_avaregion_by_gove(self.db , skip , limit , goveID)
         