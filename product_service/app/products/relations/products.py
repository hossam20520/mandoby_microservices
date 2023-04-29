from app.categorys.models import CategoryModel 
from app.units.models import UnitModel
from app.products.models import ProductModel
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import joinedload

class ProductsC:
    def __init__(self,   db  ):
        self.db = db


    def getProducts(self , skip , limit):
         q = (self.db.query(  ProductModel , CategoryModel, UnitModel )
         .join(CategoryModel , CategoryModel.id == ProductModel.category_id)
         .join(UnitModel , UnitModel.id == ProductModel.unit_id)
         .order_by(ProductModel.id.desc())
         .offset(skip)
         .limit(limit)
         .all()
         )
         data = jsonable_encoder( q)
         return data
        #  for ite in q:
        #     data = jsonable_encoder(ite)
        #     json = data['PermissionModel']
        # # print()
        #     permissions.append(json['title'])
        #  return permissions