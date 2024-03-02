import token
from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2
from sqlalchemy.orm import Session

from  database_connection import get_db
from repository.oauth2 import get_current_user
from schema_models import schemas
from repository import user_repository


router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", status_code=status.HTTP_201_CREATED)
def create(request:schemas.UserModel, db: Session = Depends(get_db)):
    return user_repository.create_users(request, db)


@router.get('/')
def get_members(db:Session=Depends(get_db)):
   return  user_repository.get_all_users(db)

@router.get("/me", response_model=schemas.TokenData)
async def read_current_user(current_user: schemas.TokenData = Depends(get_current_user)):
    return current_user

@router.get("/{id}", status_code=200)
def show(id, db: Session = Depends(get_db)):
    return user_repository.get_user_by_id(id, db)

@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_item(id, request:schemas.UserModel, db: Session = Depends(get_db)):
    return user_repository.update_user(id, request, db)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(id, db: Session = Depends(get_db)):
    return user_repository.delete_user(id, db)

# @router.get("/me", response_model=schemas.TokenData)
# async def read_current_user(current_user: schemas.TokenData = Depends(get_current_user)):
#     return current_user
@router.get("/me", response_model=schemas.TokenData)
async def read_current_user(current_user: schemas.TokenData = Depends(get_current_user)):
    return current_user
@router.post("/logout")
async def logout(token_data: schemas.TokenData = Depends(get_current_user)):
    # Here you can implement the logout logic, such as invalidating the token or updating a user's session status.
    # For simplicity, let's assume you just return a success message.
    token.invalidate_token(token_data.token)
    return {"message": "Logged out successfully"}