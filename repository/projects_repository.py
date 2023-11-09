from turtle import title
from fastapi import HTTPException, Response,status
from httpx import delete
from sqlalchemy.orm import Session
from schema_models import schemas
from database_model import models


def  create_projects(request:schemas.ProjectSchema,db:Session):

    data=models.Project(project_name=request.project_name,description=request.description,start_date=request.start_date,end_date=request.end_date,
                             estimated_budget=request.estimated_budget,status=request.status)
    db.add(data)
    db.commit()
    db.refresh(data)
    return data

def get_all_projects(db:Session):
    data=db.query(models.Project).all()
    return data



def get_single_project(id:int,db:Session):
    data=db.query(models.Project).filter(models.Project.id==id).first()
    if not data:
           raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"the Project Type with id {id} is not available",
        )
    return data
          
     
def update_single_project(id:int,request:schemas.ProjectSchema,db:Session):
    data=db.query(models.Project).filter(models.Project.id==id)
    if not data.first():
          raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"project with the id  {id} is not avaialable",
        )
    data.update(request.dict())
    db.commit()
    return "Updated successfully"



def delete_project(id:int, db:Session):
    profession = db.query(models.Project).filter(models.Project.id == id)
    if not profession.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"An project  with the id  {id} is not avaialable",
        )
    profession.delete(synchronize_session=False)
    db.commit()
    return "Successfully Deleted"