
from typing import List
from fastapi import APIRouter, Body

router = APIRouter()

@router.get("/" )
def get_all_order_managements():

    return True

