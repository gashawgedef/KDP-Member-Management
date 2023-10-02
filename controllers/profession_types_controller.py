from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from  database_connection import get_db
from schema_models import schemas
from repository import profession_types_repository


router = APIRouter(prefix="/profession_types", tags=["profession_types"])
@router.post("/", status_code=status.HTTP_201_CREATED)
def create(request:schemas.ProfessionType, db: Session = Depends(get_db)):
    return profession_types_repository.create_profession_types(request, db)


@router.get("/", status_code=status.HTTP_200_OK)
def get_all_professtion_types(db: Session = Depends(get_db)):
    return profession_types_repository.get_all_profession_types(db)


@router.get("/{id}", status_code=status.HTTP_404_NOT_FOUND)
def get_single_professtion_type(id:int,db: Session = Depends(get_db)):
    return profession_types_repository.get_single_profession_type(id,db)


@router.put("/{id}", status_code=status.HTTP_201_CREATED)
def update_profession_type(id:int, request:schemas.ProfessionType, db: Session = Depends(get_db)):
    return profession_types_repository.update_profession(id, request, db)




@router.delete("/{id}", status_code=status.HTTP_404_NOT_FOUND)
def update_profession_type(id:int, db: Session = Depends(get_db)):
    return profession_types_repository.delete_profession(id,  db)
