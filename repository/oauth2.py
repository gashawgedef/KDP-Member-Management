from multiprocessing import active_children
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated
from . import token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
# async def get_current_user(data: Annotated[str, Depends(oauth2_scheme)]):
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )
#     #token is imported from token file while data is used as a parameter
#     return token.verify_token(data,credentials_exception)
async def get_current_user(token_str: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return token.verify_token(token_str, credentials_exception)

def check_active(token_str: str = Depends(oauth2_scheme)):
    payload = token.verify_token(token_str, HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid credentials",
        headers={"WWW-Authenticate": "Bearer"}
    ))
    active = payload.get('status')
    if not active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Please activate your account first",
            headers={"WWW-Authenticate": "Bearer"}
        )
    else:
        return payload

def check_admin(token_str: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )
    payload = token.verify_token(token_str, credentials_exception)
    roles = payload.roles  # Access roles directly as an attribute

    # Check if any role has the name 'Admin'
    is_admin = any(isinstance(role, dict) and role.get('role_name') == 'Admin' for role in roles)
    if not is_admin:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Only Admin accesses this route"  
        )
    return payload

