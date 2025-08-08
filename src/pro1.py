from fastapi import FastAPI
app=FastAPI()
@app.get("/Addition")
async def addition(a: float, b: float):
    add=a+b
    return {"addition":add}
@app.get("/Subtraction")
async def subt(c: int, d: int):
    sub=d-c

    return {"subtraction":sub}
@app.get("/Multiplication")
async def mul(e: int, f: int):
    m=e*f
    return {"multiplication":m}
@app.get("/Division")
async def div(g: int, h: int):
    d=g/h
    return {"division":d}
