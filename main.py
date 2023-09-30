from fastapi import FastAPI

from schemas.Member import Members
from models import member
from controllers import members
from database.database_connection import engine

app=FastAPI()

member.database_connection.Base.metadata.create_all(engine)
app.include_router(members.router)

@app.get("/")
async def index():
    return {"Detail":"Welcome to QDAs"}

@app.post("/members")
async def register_user(members:Members):
    return  members