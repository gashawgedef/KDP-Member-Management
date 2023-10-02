from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from  database_connection import get_db
from schemas.Member import ProfessionType
from repository import profession_type


router = APIRouter(prefix="/Profession_type", tags=["Profession_type"])

@router.post("/", status_code=status.HTTP_201_CREATED)
def create(request:ProfessionType, db: Session = Depends(get_db)):
    return profession_type.create_profession_Type(request, db)
