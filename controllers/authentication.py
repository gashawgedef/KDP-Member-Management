from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from database_connection import get_db
from database_model import models
from repository import hashing, token, oauth2
from schema_models import schemas

router = APIRouter(tags=["Authentication"])

@router.post("/login")
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == request.username).first()
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )
    
    if not hashing.Hash.verify(user.password, request.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
        )

    # Assuming 'create_access_token' function works properly
    access_token = token.create_access_token(data={"sub": user.username, "id": user.id, "status": user.status})
    
    return {"access_token": access_token, "token_type": "bearer", "user": user}
