
from fastapi import HTTPException, Response,status
from sqlalchemy.orm import Session
from schemas import Member
from models import member

def create_members(request: Member.Members,db:Session):
    new_member=member.Member(
        first_name=request.first_name,middle_name=request.middle_name,last_name=request.last_name,phone=request.phone,
        email=request.email,profession=request.profession,birth_date=request.birth_date,birth_place_region=request.birth_place_region,
        birth_place_zone=request.birth_place_zone,birth_place_wereda=request.birth_place_wereda,birth_place_kebele=request.birth_place_kebele
        )
    db.add(new_member)
    db.commit()
    db.refresh(new_member)
    return new_member

def get_all_members(db:Session):
    members=db.query(member.Member).all()
    return members

def get_member_by_id(id:int,db:Session):
    member_data=db.query(member.Member).filter(member.Member.id==id)
    if not member_data:
           raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"the blog with id {id} is not available",
        )
    return member_data

def get_single_member(id:int, db:Session):
    data = db.query(member.Member).filter(member.Member.id == id).first()
    if not data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"the blog with id {id} is not available",
        )
        # response.status_code=status.HTTP_404_NOT_FOUND
        return {"detail": f"blog with the id  {id} is not avaialable"}
    return data

def update_member(id:int,request: Member.Members,db:Session):
    blog = db.query(member.Member).filter(member.Member.id == id)
    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"blog with the id  {id} is not avaialable",
        )
    blog.update(request.dict())
    db.commit()
    return "Updated successfully"




def delete_member(id, db:Session):
    blog = db.query(member.Member).filter(member.Member.id == id)
    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"blog with the id  {id} is not avaialable",
        )
    blog.delete(synchronize_session=False)
    db.commit()
    return blog