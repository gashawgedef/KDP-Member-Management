
from fastapi import Depends, HTTPException, Response,status
from sqlalchemy.orm import Session
from schema_models import schemas
from database_model import models
from .hashing import Hash
from . import token
def create_users(request: schemas.UserModel, db: Session):
    new_user = models.User(
        username=request.username,
        password=Hash.bcrypt(request.password),
        status=request.status
    )
    
    for role_data in request.roles:
        role = db.query(models.Role).filter(models.Role.role_name == role_data.role_name).first()
        if role:
            new_user.assigned_roles.append(role)
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
def get_all_users(db:Session):
    users = db.query(models.User).all()
    user_models = []
    for user in users:
        user_model = schemas.UserModel(
            username=user.username,
            password=user.password,
            status=user.status,
            roles=[schemas.RoleModel(role_name=role.role_name, description=role.description) for role in user.assigned_roles]
        )
        user_models.append(user_model)
    return user_models

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

def update_user(id:int,request: schemas.UserModel,db:Session):
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


# async def get_current_user(token_data: str = Depends(token.verify_token)):
#     return token_data

# async def get_current_active_user(current_user: schemas.TokenData = Depends(get_current_user)):
#     if not current_user.status:
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail="Inactive user",
#         )
#     return current_user