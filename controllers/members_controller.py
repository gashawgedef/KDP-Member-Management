from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from  database_connection import get_db
from schema_models import schemas
from repository import members_repository


router = APIRouter(prefix="/members", tags=["members"])

@router.post("/", status_code=status.HTTP_201_CREATED)
def create(request:schemas.Members, db: Session = Depends(get_db)):
    return members_repository.create_members(request, db)


@router.get('/')
def get_members(db:Session=Depends(get_db)):
   return  members_repository.get_all_members(db)


@router.get("/{id}", status_code=200)
def show(id, db: Session = Depends(get_db)):
    return members_repository.get_member_by_id(id, db)

@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_item(id, request:schemas. Members, db: Session = Depends(get_db)):
    return members_repository.update_member(id, request, db)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(id, db: Session = Depends(get_db)):
    return members_repository.delete_member(id, db)