from fastapi import FastAPI

from schema_models import schemas
from database_model import models
from controllers import members_controller,profession_types_controller,members_addresses_controller,donation_types_controller,announcements_controller,projects_controller,employee_tax_controllers
from database_connection import engine,Base
from fastapi import FastAPI
from  repository import members_repository
from fastapi.middleware.cors import CORSMiddleware


app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
models.Base.metadata.create_all(engine)
app.include_router(members_controller.router)
app.include_router(profession_types_controller.router)
app.include_router(members_addresses_controller.router)
app.include_router(donation_types_controller.router)
app.include_router(announcements_controller.router)
app.include_router(projects_controller.router)
app.include_router(employee_tax_controllers.router)
@app.get("/")
async def index():
    return {"Detail":"Welcome to QDAs"}

# @app.post("/members")
# async def register_user(members:Members):
#     return  members