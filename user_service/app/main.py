from fastapi import Depends, FastAPI, HTTPException ,  Request
import app.users.models as models
import app.permissions.models as permission_model 
from app.users.routes import router as user_router
from app.permissions.routes import router as permission_router
from app.roles.routes import router as roles_router
from app.role_users.routes import router as role_users_router
from app.permission_roles.routes import router as permission_roles_router
from app.database import SessionLocal, engine , session , Base
from app.auth.login import router as login_router
from app.auth.register import router as register_router
import time
import os 
# from fastapi.middleware.cors import CORSMiddleware
from app.governorates.routes import router as governorates_router 
from app.regions.routes import router as regions_router 
from fastapi.middleware.trustedhost import TrustedHostMiddleware

from starlette.middleware.cors import CORSMiddleware
from starlette.middleware import Middleware

models.Base.metadata.create_all(bind=engine)
# permission_model.Base.metadata.create_all(bind=engine)

# origins = ["*"]


# middleware = [
#     Middleware(
#         CORSMiddleware,
#         allow_origins=['*'],
#         allow_credentials=True,
#         allow_methods=['*'],
#         allow_headers=['*']
#     )
# ]

# middleware = [
#     Middleware(CORSMiddleware, allow_origins=origins)
# ]



# origins = ["*"]

# middleware = [
#     Middleware(CORSMiddleware, allow_origins=origins)
# ]

# app = FastAPI(middleware=middleware)


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




# @app.middleware("http")
# async def print_request(request: Request, call_next):
#     print("Middleware executed")
#     response = await call_next(request)
#     return response

# @app.middleware("http")
# async def add_process_time_header(request: Request, call_next):
#     start_time = time.time()
#     response = await call_next(request)
#     process_time = time.time() - start_time
#     response.headers["X-Process-Time"] = str(process_time)
#     return response


app.include_router(login_router, tags=["login"], prefix="/api/v1.0/login")
app.include_router(register_router, tags=["register"], prefix="/api/v1.0/register")
app.include_router(user_router, tags=["Users"], prefix="/api/v1.0/users")
app.include_router(permission_router, tags=["Permissions"], prefix="/api/v1.0/permissions")
app.include_router(roles_router, tags=["Roles"], prefix="/api/v1.0/roles")
app.include_router(permission_roles_router, tags=["Permission_role"], prefix="/api/v1.0/permission_role")
app.include_router(role_users_router, tags=["Role_users"], prefix="/api/v1.0/role_users")

# 

app.include_router(governorates_router, tags=["Governorates"], prefix="/api/v1.0/governorates") 
app.include_router(regions_router, tags=["Regions"], prefix="/api/v1.0/regions") 



# @app.middleware("http")
# async def add_process_time_header(request: Request, call_next):
#     start_time = time.time()
#     response = await call_next(request)
#     process_time = time.time() - start_time
#     response.headers["X-Process-Time"] = str(process_time)
#     return response










#from sqlalchemy_seed import (
    #create_table,
    #drop_table,
    #load_fixtures,
    #load_fixture_files,
    #)


# def main():
#     path =  os.getcwd() 
#     fixtures = load_fixture_files(path, ['seeds.yaml'])
#     load_fixtures(session, fixtures)

# main()
