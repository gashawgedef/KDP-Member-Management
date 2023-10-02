from fastapi import FastAPI

from schemas.Member import Members
from models import member
from controllers import members,profession_type
from database_connection import engine,Base


app=FastAPI()

member.Base.metadata.create_all(engine)
app.include_router(members.router)
app.include_router(profession_type.router)

@app.get("/")
async def index():
    return {"Detail":"Welcome to QDAs"}

# @app.post("/members")
# async def register_user(members:Members):
#     return  members