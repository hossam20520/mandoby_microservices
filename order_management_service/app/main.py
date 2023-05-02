
from app.database import SessionLocal, engine
from fastapi import Depends, FastAPI, HTTPException ,  Request 
# from app.order_managements.routes import router as order_managements_router 
from app.orders.routes import router as orders_router 
# from app.shippings.routes import router as shippings_router 
from app.payments.routes import router as payments_router 
from app.orders.models import OrderModel as modls
from app.avagovs.routes import router as avagovs_router 
from app.avaregions.routes import router as avaregions_router 
from app.addresses.routes import router as addresses_router
# modls.Base.metadata.create_all(bind=engine)





app = FastAPI()
app.include_router(payments_router, tags=["Payment"], prefix="/api/v1.0/payment") 
app.include_router(addresses_router, tags=["address"], prefix="/api/v1.0/addresses") 
app.include_router(orders_router, tags=["Orders"], prefix="/api/v1.0/orders") 
app.include_router(avagovs_router, tags=["Avagovs"], prefix="/api/v1.0/avagovs") 
app.include_router(avaregions_router, tags=["Avaregions"], prefix="/api/v1.0/avaregions") 