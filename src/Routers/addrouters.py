from fastapi import APIRouter
from src.api.add import add
router=APIRouter(tags=[" "])
@router.get("/add/")
def addition(a:int,b:int):
    c=a+b
    return c