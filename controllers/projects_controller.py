


from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from  database_connection import get_db
from schema_models import schemas
from repository import projects_repository


router = APIRouter(prefix="/projects", tags=["projects"])

@router.post("/", status_code=status.HTTP_201_CREATED)
def create(request:schemas.ProjectSchema, db: Session = Depends(get_db)):
    return projects_repository.create_projects(request, db)


@router.get('/')
def get_all_project(db:Session=Depends(get_db)):
    return projects_repository.get_all_projects(db)

@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_project(id, request:schemas.ProjectSchema, db: Session = Depends(get_db)):
    return projects_repository.update_single_project(id, request, db)


@router.get("/{id}", status_code=status.HTTP_404_NOT_FOUND)
def get_single_project(id:int,db: Session = Depends(get_db)):
    return projects_repository.get_single_project(id,db)

@router.delete("/{id}", status_code=status.HTTP_404_NOT_FOUND)
def delete_project(id:int, db: Session = Depends(get_db)):
    return projects_repository.delete_project(id,  db)

