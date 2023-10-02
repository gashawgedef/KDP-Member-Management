from fastapi import HTTPException, Response,status
from sqlalchemy.orm import Session
from schemas.Member import ProfessionType
from models import member


def create_profession_Type(request: ProfessionType,db:Session):
    new_member=member.ProfessionType(
        
     profession_name=request.profession_name,
     profession_description=request.profession_description

       )
    db.add(new_member)
    db.commit()
    db.refresh(new_member)
    return new_member