


from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from  database_connection import get_db
from schema_models import schemas
from repository import announcements_repository


router = APIRouter(prefix="/anouncements", tags=["anouncements"])

@router.post("/", status_code=status.HTTP_201_CREATED)
def create(request:schemas.AnouncementSchema, db: Session = Depends(get_db)):
    return announcements_repository.create_announcements(request, db)


@router.get('/')
def get_all_announcements(db:Session=Depends(get_db)):
    return announcements_repository.get_all_Announcements(db)

@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_announcement(id, request:schemas.AnouncementSchema, db: Session = Depends(get_db)):
    return announcements_repository.update_single_announcement(id, request, db)


@router.get("/{id}", status_code=status.HTTP_404_NOT_FOUND)
def get_single_announcement(id:int,db: Session = Depends(get_db)):
    return announcements_repository.get_single_announcement(id,db)


@router.delete("/{id}", status_code=status.HTTP_404_NOT_FOUND)
def delete_announcement(id:int, db: Session = Depends(get_db)):
    return announcements_repository.delete_announcement(id,  db)

