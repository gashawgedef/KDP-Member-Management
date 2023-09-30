
from fastapi import HTTPException, Response,status
from sqlalchemy.orm import Session
from ..schemas import Member
from ..models import member
def create_members(request: Member.Members,db:Session):
    new_member=Member.Members(
        first_name=request.first_name,middle_name=request.middle_name,last_name=request.last_name,phone=request.phone,
        email=request.email,profession=request.profession,birth_date=request.birth_date,birth_place_region=request.birth_place_region,
        birth_place_zone=request.birth_place_zone,birth_place_wereda=request.birth_place_wereda,birth_place_kebele=request.birth_place_kebele
        )
    db.add(new_member)
    db.commit()
    db.refresh(new_member)
    return new_member
