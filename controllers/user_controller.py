from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from  database_connection import get_db
from schema_models import schemas
from repository import user_repository


router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", status_code=status.HTTP_201_CREATED)
def create(request:schemas.User, db: Session = Depends(get_db)):
    return user_repository.create_users(request, db)


@router.get('/')
def get_members(db:Session=Depends(get_db)):
   return  user_repository.get_all_users(db)


@router.get("/{id}", status_code=200)
def show(id, db: Session = Depends(get_db)):
    return user_repository.get_user_by_id(id, db)

@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_item(id, request:schemas.Members, db: Session = Depends(get_db)):
    return user_repository.update_user(id, request, db)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(id, db: Session = Depends(get_db)):
    return user_repository.delete_user(id, db)