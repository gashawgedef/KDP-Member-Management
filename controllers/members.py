from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from ..database.database_connection import get_db
from ..schemas.Member import Members
from ..repository import members

router = APIRouter(prefix="/members", tags=["members"])

@router.post("/", status_code=status.HTTP_201_CREATED)
def create(request:Members, db: Session = Depends(get_db)):
    return members.create_members(request, db)