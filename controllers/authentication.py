
from fastapi import APIRouter, Depends, status,HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from  database_connection import get_db
from database_model import models
from repository import hashing
from schema_models  import schemas
from repository import token
router = APIRouter( tags=["Authentication"])

@router.post("/login")
def Login(request:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    user=db.query(models.User).filter(models.User.username==request.username).first()
    if user:
        print(user)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"The user with user name not found",
        )
    if not hashing.Hash.verify(user.password,request.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Invalid Credintials",
        )
  
    roles = [role.role_name for role in user.assigned_roles]  # Assuming 'role_name' is the attribute you want to include
    access_token = token.create_access_token(data={"sub": user.username, "id": user.id, "roles": roles,"status":user.status})
    return {"access_token": access_token, "token_type": "Bearer"}