import requests 
from app.avaregions import crud

class RegionService:
    def __init__(self , db):
         self.db = db 
    

    def getRegions(self , skip=0 , limit=100 , goveID = 1):
         return crud.get_avaregion_by_gove(self.db , skip , limit , goveID)
         