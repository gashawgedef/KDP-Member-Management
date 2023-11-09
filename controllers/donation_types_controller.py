

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from  database_connection import get_db
from schema_models import schemas
from repository import donation_types_repository


router = APIRouter(prefix="/donation_types", tags=["donation_types"])

@router.post("/", status_code=status.HTTP_201_CREATED)
def create(request:schemas.DanationTypeSchema, db: Session = Depends(get_db)):
    return donation_types_repository.create_donation_types(request, db)

@router.get('/')
def get_all_donation_types(db:Session=Depends(get_db)):
    return donation_types_repository.get_all_Donations(db)

@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_donation_type(id, request:schemas.DanationTypeSchema, db: Session = Depends(get_db)):
    return donation_types_repository.update_single_donation(id, request, db)


@router.get("/{id}", status_code=status.HTTP_404_NOT_FOUND)
def get_single_donation_type(id:int,db: Session = Depends(get_db)):
    return donation_types_repository.get_single_donation_type(id,db)


@router.delete("/{id}", status_code=status.HTTP_404_NOT_FOUND)
def update_profession_type(id:int, db: Session = Depends(get_db)):
    return donation_types_repository.delete_donation_type(id,  db)

