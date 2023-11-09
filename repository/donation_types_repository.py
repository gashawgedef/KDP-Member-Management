from fastapi import HTTPException, Response,status
from httpx import delete
from sqlalchemy.orm import Session
from schema_models import schemas
from database_model import models


def  create_donation_types(request:schemas.DanationTypeSchema,db:Session):

    data=models.DonationType(donation_name=request.donation_name,description=request.description)
    db.add(data)
    db.commit()
    db.refresh(data)
    return data

def get_all_Donations(db:Session):
    data=db.query(models.DonationType).all()
    return data



def get_single_donation_type(id:int,db:Session):
    data=db.query(models.DonationType).filter(models.DonationType.id==id).first()
    if not data:
           raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"the Donation Type with id {id} is not available",
        )
    return data
          
     
def update_single_donation(id:int,request:schemas.DanationTypeSchema,db:Session):
    data=db.query(models.DonationType).filter(models.DonationType.id==id)
    if not data.first():
          raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"blog with the id  {id} is not avaialable",
        )
    data.update(request.dict())
    db.commit()
    return "Updated successfully"



def delete_donation_type(id:int, db:Session):
    profession = db.query(models.DonationType).filter(models.DonationType.id == id)
    if not profession.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Profession Type  with the id  {id} is not avaialable",
        )
    profession.delete(synchronize_session=False)
    db.commit()
    return "Successfully Deleted"