from typing import List
from fastapi import APIRouter, Body
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import app.users.models as models
import app.users.crud as crud 
import app.permissions.crud as permission_crud
import app.roles.crud as roles_crud
import app.permission_roles.crud as permission_role_crud
import app.role_users.crud as role_user_crud
from app.users.schemas import UserInfo
from app.users.schemas import UserCreate , User
from app.database import SessionLocal, engine
from app.global_schemas import ResponseModel , ResponseModelSchema
from app.auth.RoleChecker import  RoleCheckerByToken
from app.auth.jwt_bearer import JWTBearer , decodeJWT
from fastapi.security import OAuth2PasswordBearer
import json
import requests
from app.auth.register import CheckDubulcatedRecords
from fastapi.encoders import jsonable_encoder

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
router = APIRouter()
 





# @router.get("/seeds/all")
# def create_all_seeds( db: Session = Depends(get_db)  ):
#     fusers = open('users.json')
#     fpermissions = open('permissions.json')
#     froles = open('roles.json')
#     fpermission_roles = open('permission_roles.json')
#     frole_users = open('role_users.json')

#     data_user = json.load(fusers)  
#     data_permissions = json.load(fpermissions) 
#     data_roles = json.load(froles) 
#     data_permission_roles = json.load(fpermission_roles)   
#     data_users = json.load(frole_users)



#     crud.create_user_seeds(db, data_user)   
#     permission_crud.create_permission_seeds(db, data_permissions)
#     roles_crud.create_roles_seeds(db, data_roles)
#     permission_role_crud.create_permission_role_seeds(db, data_permission_roles)
#     role_user_crud.create_user_role_seeds(db, data_users)
#     return "success"



@router.get("/seeds")
def create_user_seeds( db: Session = Depends(get_db)  ):
    f = open('app/users.json')
    data = json.load(f)   
    return crud.create_user_seeds(db, data)


@router.get("/test" )
def test_all_user(db: Session = Depends(get_db) ):
    response = requests.get('http://product_service:8000/api/v1.0/categorys/?skip=0&limit=100')
    data = json.loads(response.text)

    # crud.delete_all_user(db)
    # http://localhost:8080/api/v1.0/categorys/?skip=0&limit=100
    # raise  HTTPException(200, ResponseModel([] , "All Users Deleted" , True , 200 , {})) from None
    return data



# @router.post("/info", dependencies=[ Depends( JWTBearer())])
# def get_info_user( db: Session = Depends(get_db) , token: str = Depends(oauth2_scheme) ):
#     # Start RoleCheckerByToken
#     userToken = decodeJWT(token)
#     print(userToken)
#     # allow_access = RoleCheckerByToken(token, "users" , db , "read__users")
#     # allow_access.__call__(userToken['user_id']['id'])
#     # End RoleCheckerByToken
#     # users = crud.get_users(db, skip=skip, limit=limit)
#     return 55

@router.get("/info", response_model=UserInfo ,  dependencies=[ Depends( JWTBearer())])
def get_info_user( db: Session = Depends(get_db) , token: str = Depends(oauth2_scheme)):
    # Start RoleCheckerByToken
    userToken = decodeJWT(token)
    allow_access = RoleCheckerByToken(token, "users" , db , "show__user")
    role = allow_access.geRole(userToken['user_id']['id'])
    permissions = allow_access.getPermissionsByTitle(role)
    # End RoleCheckerByToken
    db_user = crud.get_user(db, user_id=userToken['user_id']['id'])
    return_model = {
        "id": db_user.id,
        "name":db_user.first_name + " " + db_user.last_name,
        "first_name": db_user.first_name,
        "last_name": db_user.last_name,
        "username": db_user.username,
        "email": db_user.email,
        "phone": db_user.phone,
        "is_active": db_user.is_active,
        "roles": [role],
        "permissions":permissions
     }
    if db_user is None:
        raise HTTPException(status_code=404, detail=ResponseModel([] , "User not found" , True , 404 , {}))
    return return_model



@router.get("/pagentation" , dependencies=[ Depends( JWTBearer())])
def get_all_users_pagenation(skip: int = 0, limit: int = 100, db: Session = Depends(get_db) , token: str = Depends(oauth2_scheme) ):
    # Start RoleCheckerByToken
    userToken = decodeJWT(token)
    allow_access = RoleCheckerByToken(token, "users" , db , "read__users")
    allow_access.__call__(userToken['user_id']['id'])
    # End RoleCheckerByToken
    users = crud.get_users_pagentation(db, skip=skip, limit=limit)
    return users


@router.get("/", response_model=List[User] , dependencies=[ Depends( JWTBearer())])
def get_all_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db) , token: str = Depends(oauth2_scheme) ):
    # Start RoleCheckerByToken
    userToken = decodeJWT(token)
    allow_access = RoleCheckerByToken(token, "users" , db , "read__users")
    allow_access.__call__(userToken['user_id']['id'])
    # End RoleCheckerByToken
    users = crud.get_users(db, skip=skip, limit=limit)
    return users





@router.post("/", response_model=User ,  dependencies=[ Depends( JWTBearer())])
def create_user(user: UserCreate, db: Session = Depends(get_db) ,  token: str = Depends(oauth2_scheme) ):
    # Start RoleCheckerByToken
    userToken = decodeJWT(token)
    allow_access = RoleCheckerByToken(token, "users" , db , "create__user")
    allow_access.__call__(userToken['user_id']['id'])
    # End RoleCheckerByToken
    return crud.create_user(db=db, user=user)
    
#JWTBearer
@router.delete("/" ,  dependencies=[ Depends( JWTBearer())] )
def delete_all_users(db: Session = Depends(get_db) , token: str = Depends(oauth2_scheme)):
    # Start RoleCheckerByToken
    userToken = decodeJWT(token)
    allow_access = RoleCheckerByToken(token, "users" , db , "delete__users")
    allow_access.__call__(userToken['user_id']['id'])
    # End RoleCheckerByToken
    crud.delete_all_user(db)
    raise  HTTPException(200, ResponseModel([] , "All Users Deleted" , True , 200 , {})) from None

@router.get("/{user_id}", response_model=User ,  dependencies=[ Depends( JWTBearer())])
def get_one_user(user_id: int, db: Session = Depends(get_db) , token: str = Depends(oauth2_scheme)):
    # Start RoleCheckerByToken
    userToken = decodeJWT(token)
    allow_access = RoleCheckerByToken(token, "users" , db , "show__user")
    allow_access.__call__(userToken['user_id']['id'])
    # End RoleCheckerByToken
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail=ResponseModel([] , "User not found" , True , 404 , {}))
    return db_user

@router.put("/{id}" ,  dependencies=[ Depends( JWTBearer())])
def update_user(id:int ,db: Session = Depends(get_db) , user: UserCreate = Body(...) ,  token: str = Depends(oauth2_scheme)):
    # Start RoleCheckerByToken
    userToken = decodeJWT(token)
    allow_access = RoleCheckerByToken(token, "users" , db , "update__user")
    allow_access.__call__(userToken['user_id']['id'])
    # End RoleCheckerByToken
    data = jsonable_encoder(user)
    # CheckDubulcatedRecords(db ,  data )
    db_user = crud.update_user(db, user   ,id)
    return  db_user

@router.delete("/{id}" ,  dependencies=[ Depends( JWTBearer())]  )
def delete_one_user(id:int ,db: Session = Depends(get_db) ,  token: str = Depends(oauth2_scheme)):
	# Start RoleCheckerByToken
    userToken = decodeJWT(token)
    allow_access = RoleCheckerByToken(token, "users" , db , "delete__user")
    allow_access.__call__(userToken['user_id']['id'])
    # End RoleCheckerByToken
    db_user = crud.delete_user(db,id)
    return  db_user
