
from fastapi import HTTPException, Response,status
from sqlalchemy.orm import Session
from schema_models import schemas
from database_model import models
from .hashing import Hash
def create_users(request: schemas.User,db:Session):
    new_user=models.User(
        username=request.username,role=request.role,password=Hash.bcrypt(request.password),status=request.status
        )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_all_users(db:Session):
    users=db.query(models.User).all()
    return users

def get_user_by_id(id:int,db:Session):
    member_data=db.query(models.User).filter(models.User.id==id)
    if not member_data.first():
           raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"the user with id {id} is not available",
        )
    return member_data

def get_single_employee_tax(id:int, db:Session):
    data = db.query(models.User).filter(models.User.id == id).first()
    if not data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"the user  with id {id} is not available",
        )
    
    return data

def update_user(id:int,request: schemas.User,db:Session):
    user = db.query(models.User).filter(models.User.id == id)
    if not user.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"user  with the id  {id} is not avaialable",
        )
    user.update(request.dict())
    db.commit()
    return "Updated successfully"




def delete_user(id, db:Session):
    user = db.query(models.User).filter(models.User.id == id)
    if not user.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"user with the id  {id} is not avaialable in the database",
        )
    user.delete(synchronize_session=False)
    db.commit()
    return user


def  get_these():
    return {"detail":"Gashaw Gedef"}