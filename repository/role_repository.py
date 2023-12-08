
from fastapi import HTTPException, Response,status
from sqlalchemy.orm import Session
from schema_models import schemas
from database_model import models

def create_roles(request: schemas.RoleModel,db:Session):
    new_role=models.Role(
        role_name=request.role_name,description=request.description
        )
    db.add(new_role)
    db.commit()
    db.refresh(new_role)
    return new_role

def get_all_roles(db:Session):
    roles=db.query(models.Role).all()
    return roles

def get_role_by_id(id:int,db:Session):
    role_data=db.query(models.Role).filter(models.Role.id==id)
    if not role_data.first():
           raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"the role with id {id} is not available",
        )
    return role_data


def update_role(id:int,request: schemas.RoleModel,db:Session):
    role = db.query(models.Role).filter(models.Role.id == id)
    if not role.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"role  with the id  {id} is not avaialable",
        )
    role.update(request.dict())
    db.commit()
    return "Updated successfully"




def delete_role(id, db:Session):
    role = db.query(models.Role).filter(models.Role.id == id)
    if not role.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"role with the id  {id} is not avaialable in the database",
        )
    role.delete(synchronize_session=False)
    db.commit()
    return role

