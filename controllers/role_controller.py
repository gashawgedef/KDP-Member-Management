from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from  database_connection import get_db
from schema_models import schemas
from repository import role_repository


router = APIRouter(prefix="/roles", tags=["roles"])

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_role(request:schemas.RoleModel, db: Session = Depends(get_db)):
    return role_repository.create_roles(request, db)


@router.get('/')
def get_roles(db:Session=Depends(get_db)):
   return  role_repository.get_all_roles(db)


@router.get("/{id}", status_code=200)
def show_role_by_id(id, db: Session = Depends(get_db)):
    return role_repository.get_role_by_id(id, db)

@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_role(id, request:schemas.Members, db: Session = Depends(get_db)):
    return role_repository.update_role(id, request, db)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_role(id, db: Session = Depends(get_db)):
    return role_repository.delete_role(id, db)