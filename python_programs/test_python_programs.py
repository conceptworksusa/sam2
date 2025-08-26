# from fastapi import FastAPI
#
# app = FastAPI()
#
#
# @app.get("/items/{item_id}")
# async def read_item(item_id):
#     return {"item_id": item_id}

#----------------------------------------------------------------------

# import logging
# logging.basicConfig(level=logging.INFO)
# logging.info("sampurna")


#----------------------------------------------------------------------

# hello_router.py

# from fastapi import APIRouter
#
# router = APIRouter()
#
# @router.get("/hello")
# def say_hello():
#     return {"message": "Hello!"}
#
# @router.get("/users/{user_id}")
# def get_user(user_id: int):
#     return {"id": user_id, "name": "User Name"}


from fastapi import APIRouter
router=APIRouter()
@router.get("/hello")
def say():
    return {"message":"hello world"}
@router.get("/users/{id}")
def user(userid:int):
    return {"id":id,"name":"name"}




