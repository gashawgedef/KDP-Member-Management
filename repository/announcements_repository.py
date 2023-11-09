from turtle import title
from fastapi import HTTPException, Response,status
from httpx import delete
from sqlalchemy.orm import Session
from schema_models import schemas
from database_model import models


def  create_announcements(request:schemas.AnouncementSchema,db:Session):

    data=models.Announcement(title=request.title,content=request.content,posted_date=request.posted_date)
    db.add(data)
    db.commit()
    db.refresh(data)
    return data

def get_all_Announcements(db:Session):
    data=db.query(models.Announcement).all()
    return data



def get_single_announcement(id:int,db:Session):
    data=db.query(models.Announcement).filter(models.Announcement.id==id).first()
    if not data:
           raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"the Anouncement Type with id {id} is not available",
        )
    return data
          
     
def update_single_announcement(id:int,request:schemas.AnouncementSchema,db:Session):
    data=db.query(models.Announcement).filter(models.Announcement.id==id)
    if not data.first():
          raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"blog with the id  {id} is not avaialable",
        )
    data.update(request.dict())
    db.commit()
    return "Updated successfully"



def delete_announcement(id:int, db:Session):
    profession = db.query(models.Announcement).filter(models.Announcement.id == id)
    if not profession.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"An anouncement  with the id  {id} is not avaialable",
        )
    profession.delete(synchronize_session=False)
    db.commit()
    return "Successfully Deleted"