from fastapi import HTTPException, Response,status
from sqlalchemy.orm import Session
from schema_models import schemas
from database_model import models


def create_members_address(request: schemas.MembersAddress,db:Session):
    data=models.MemberAddress(
          name=request.name,
          country=request.country,
          address_region=request.address_region,
          address_zone=request.address_zone,
          address_wereda=request.address_wereda,
          annual_contribution=request.annual_contribution,
          membership_year=request.membership_year
       
        )
    db.add(data)
    db.commit()
    db.refresh(data)
    return data