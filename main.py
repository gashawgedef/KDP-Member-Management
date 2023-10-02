from fastapi import FastAPI

from schema_models import schemas
from database_model import models
from controllers import members_controller,profession_types_controller
from database_connection import engine,Base
from fastapi import FastAPI
from  repository import members_repository


app=FastAPI()

models.Base.metadata.create_all(engine)
app.include_router(members_controller.router)
app.include_router(profession_types_controller.router)

@app.get("/")
async def index():
    return {"Detail":"Welcome to QDAs"}

# @app.post("/members")
# async def register_user(members:Members):
#     return  members