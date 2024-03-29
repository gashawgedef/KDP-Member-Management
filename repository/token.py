

from datetime import datetime, timedelta
from msilib import schema
import token
from typing import Annotated, List
from fastapi import Depends
from jose import JWTError, jwt
from schema_models import schemas


SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30



def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# def verify_token(token: str, credentials_exception):
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         username: str = payload.get("sub")
#         user_id: int = payload.get("id")
#         status: bool = payload.get("status")
#         if username is None or user_id is None or status is None:
#             raise credentials_exception
#         token_data = schemas.TokenData(username=username, id=user_id, status=status)
#     except JWTError:
#         raise credentials_exception
#     return token_data
def verify_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        user_id: int = payload.get("id")
        status: bool = payload.get("status")
        roles: List[schemas.RoleModel] = payload.get("roles", [])
        if None in (username, user_id, status):
            raise credentials_exception
        
        token_data = schemas.TokenData(
            username=username,
            id=user_id,
            status=status,
            roles=roles
            # Include more fields as necessary
        )
    except JWTError:
        raise credentials_exception
    return token_data

# def check_active(token:str=Depends(oa)):


