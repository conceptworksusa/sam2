from fastapi import FastAPI
app=FastAPI()
@app.get("/addition/")
async def add(b: int, a: int):
    c=a+b
    return {"addition":c}