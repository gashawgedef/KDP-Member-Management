from typing import Annotated, Optional
from fastapi import APIRouter, BackgroundTasks, Depends, Query, Response, status
from sqlalchemy.orm import Session

from  database_connection import get_db
from schema_models import schemas
from repository import members_repository,oauth2


router = APIRouter(prefix="/members", tags=["members"])

@router.post("/", status_code=status.HTTP_201_CREATED)
def create(request: schemas.Members, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    return members_repository.create_members(request, db, background_tasks)

#,current_user:schemas.UserModel=Depends(oauth2.get_current_user)
@router.get('/')
def get_members(
    first_name: str = Query(None, description="Filter by first name"),
    status: str = Query(None, description="Filter by status"),
    page: int = Query(1, ge=1, description="Page number"),
    per_page: int = Query(20, ge=1, description="Items per page"),
    db: Session = Depends(get_db)
):
    pagination_params = schemas.Pagination(page=page, perPage=per_page)
    return members_repository.get_all_members(db, pagination_params, first_name=first_name, status=status)

@router.get("/export/members/excel")
async def export_members_excel(
    response: Response,
    db: Session = Depends(get_db),
    first_name: Optional[str] = Query(None, description="Filter by first name"),
    status: Optional[str] = Query(None, description="Filter by status"),
):
    return await members_repository.export_members_excel(db, first_name=first_name, status=status)

    
@router.get("/{id}", status_code=200)
def show(id, db: Session = Depends(get_db)):
    return members_repository.get_single_member(id, db)

@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_item(id, request:schemas.Members, db: Session = Depends(get_db),current_user:schemas.UserModel=Depends(oauth2.get_current_user)):
    return members_repository.update_member(id, request, db)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(id, db: Session = Depends(get_db),current_user:schemas.UserModel=Depends(oauth2.get_current_user)):
    return members_repository.delete_member(id, db)

@router.post("/send-notification/{email}")
async def send_notification(
    email: str, background_tasks: BackgroundTasks, q: Annotated[str, Depends(members_repository.get_query)]
):
    message = f"message to {email}\n"
    background_tasks.add_task(members_repository.write_log, message)
    return {"message": "Message sent"}