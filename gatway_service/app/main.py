from fastapi import Depends, FastAPI, HTTPException ,  Request 
from  app.gateways.routes import router as gateways_router 
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware import Middleware
from app.users_gateway.routes import router as users_gatway_router
from app.roles_gateway.routes import router as roles_gatway_router
from app.products_gateway.routes  import router as product_gatway_router
from app.units_gateway.routes import router as units_gatway_router
from app.cart_gateway.routes import router as carts_gatway_router
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# models_gateways.Base.metadata.create_all(bind=engine) 


app.include_router(gateways_router, tags=["Gateways"], prefix="/api/v1.0/gateways") 
app.include_router(users_gatway_router, tags=["users_gatway"], prefix="/api/v1.0/gateway/users") 
app.include_router(roles_gatway_router, tags=["roles_gatway"], prefix="/api/v1.0/gateway/roles") 
app.include_router(units_gatway_router, tags=["units_gatway"], prefix="/api/v1.0/gateway/units") 
app.include_router(product_gatway_router, tags=["products_gatway"], prefix="/api/v1.0/gateway/products") 
app.include_router(carts_gatway_router, tags=["carts_gatway"], prefix="/api/v1.0/gateway/carts") 