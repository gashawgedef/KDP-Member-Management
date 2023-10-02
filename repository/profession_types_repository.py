
from fastapi import HTTPException, Response,status
from sqlalchemy.orm import Session
from schema_models import schemas
from database_model import models

def create_profession_types(request: schemas.ProfessionType,db:Session):
    new_member=models.ProfessionType(
        profession_name=request.profession_name,description=request.profession_description)
    db.add(new_member)
    db.commit()
    db.refresh(new_member)
    return new_member

def get_all_profession_types(db:Session):
    data=db.query(models.ProfessionType).all()
    return data
