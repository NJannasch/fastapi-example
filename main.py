from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from businesslogic import get_id

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/signup")
async def signup():
    return {"message": "Please sign up"}

@app.get("/users")
async def users():
    return {"users": [get_id(), get_id(), get_id()]}
