import requests 


class RegionService:
    def __init__(self):
         self.baseURL = "http://order_management_service:8000"

    def getRegions(self , skip=0 , limit=100 , goveID = 1):
         response = requests.get(self.baseURL+f"/api/v1.0/avaregions/regions/{goveID}?skip={skip}&limit={limit}"  )
         return response.json()
     #     return crud.get_avaregion_by_gove(self.db , skip , limit , goveID)
         