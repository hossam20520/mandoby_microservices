
from app.database import SessionLocal, engine
from fastapi import Depends, FastAPI, HTTPException ,  Request 
import app.products.models as models_products 
from app.products.routes import router as products_router 
from app.categorys.routes import router as categorys_router 
import app.categorys.models as models_categorys 
import app.units.models as models_units 
from app.units.routes import router as units_router 
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware import Middleware
from app.carts.routes import router as carts_router 

models_units.Base.metadata.create_all(bind=engine) 
models_categorys.Base.metadata.create_all(bind=engine) 
models_products.Base.metadata.create_all(bind=engine) 



app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(carts_router, tags=["Carts"], prefix="/api/v1.0/carts")
app.include_router(categorys_router, tags=["Categorys"], prefix="/api/v1.0/categorys") 
app.include_router(units_router, tags=["Units"], prefix="/api/v1.0/units") 
app.include_router(products_router, tags=["Products"], prefix="/api/v1.0/products") 