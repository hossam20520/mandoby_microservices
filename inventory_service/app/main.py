
from app.database import SessionLocal, engine
from fastapi import Depends, FastAPI, HTTPException ,  Request 
import app.inventorys.models as models_inventorys 
from app.inventorys.routes import router as inventorys_router 
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware import Middleware

# models_inventorys.Base.metadata.create_all(bind=engine) 

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



app.include_router(inventorys_router, tags=["Inventorys"], prefix="/api/v1.0/inventorys") 
