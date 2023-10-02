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

