
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


def get_single_profession_type(id:int,db:Session):
    data=db.query(models.ProfessionType).filter(models.ProfessionType.id==id).first()
    if not data:
           raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"the blog with id {id} is not available",
        )
    return data



def update_profession(id:int,request: schemas.ProfessionType,db:Session):
    blog = db.query(models.ProfessionType).filter(models.ProfessionType.id == id)
    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"blog with the id  {id} is not avaialable",
        )
    blog.update(request.dict())
    db.commit()
    return "Updated successfully"
    



def delete_profession(id:int, db:Session):
    profession = db.query(models.ProfessionType).filter(models.ProfessionType.id == id)
    if not profession.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Profession Type  with the id  {id} is not avaialable",
        )
    profession.delete(synchronize_session=False)
    db.commit()
    return "Successfully Deleted"