from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from  database_connection import get_db
from schema_models import schemas
from repository import receipt_items_repository,oauth2


router = APIRouter(prefix="/reciept_items", tags=["reciept_items"])

@router.post("/", status_code=status.HTTP_201_CREATED)
def create(request:schemas.RecieptItemsModel, db: Session = Depends(get_db)):
    return receipt_items_repository.create_reciept_items(request, db)

#,current_user:schemas.UserModel=Depends(oauth2.get_current_user)
@router.get('/')
def get_members(db:Session=Depends(get_db)):
   return  receipt_items_repository.get_all_reciept_items(db)


@router.get("/{id}", status_code=200)
def show(id, db: Session = Depends(get_db)):
    return receipt_items_repository.get_single_reciept_item(id, db)

@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_item(id, request:schemas.RecieptIssuerModel, db: Session = Depends(get_db),current_user:schemas.UserModel=Depends(oauth2.get_current_user)):
    return receipt_items_repository.update_reciept_item(id, request, db)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(id, db: Session = Depends(get_db),current_user:schemas.UserModel=Depends(oauth2.get_current_user)):
    return receipt_items_repository.delete_reciept_item(id, db)