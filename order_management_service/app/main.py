
from app.database import SessionLocal, engine
from fastapi import Depends, FastAPI, HTTPException ,  Request 
import app.order_managements.models as models_order_managements 
from app.order_managements.routes import router as order_managements_router 
from app.orders.routes import router as orders_router 
from app.shippings.routes import router as shippings_router 
from app.payments.routes import router as payments_router 






app = FastAPI()
app.include_router(orders_router, tags=["Orders"], prefix="/api/v1.0/orders") 
app.include_router(shippings_router, tags=["Shippings"], prefix="/api/v1.0/shippings") 
app.include_router(order_managements_router, tags=["Order_managements"], prefix="/api/v1.0/order_managements") 
app.include_router(payments_router, tags=["Payments"], prefix="/api/v1.0/payments") 