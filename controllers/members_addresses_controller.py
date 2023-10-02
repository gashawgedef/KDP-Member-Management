from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from  database_connection import get_db
from schema_models import schemas
from repository import member_address_repository




router = APIRouter(prefix="/member_addresses", tags=["member_addresses"])
@router.post("/", status_code=status.HTTP_201_CREATED)
def create(request:schemas.MembersAddress, db: Session = Depends(get_db)):
    return member_address_repository.create_members_address(request, db)