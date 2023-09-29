from fastapi import FastAPI

from schemas.Member import Members

app=FastAPI()

@app.get("/")
async def index():
    return {"Detail":"Welcome to QDA"}

@app.post("/members")
async def register_user(members:Members):
    return  members