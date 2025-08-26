from fastapi import FastAPI
from src.Routers.addrouters import router as add_router
from src.Routers.subrouter import router as sub_router

# initiating app router
app=FastAPI()

# Adding individual rouetrs
app.include_router(add_router)
app.include_router(sub_router)
