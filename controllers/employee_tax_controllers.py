from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from  database_connection import get_db
from schema_models import schemas
from repository import employee_tax_repository


router = APIRouter(prefix="/emplyee_tax", tags=["emplyee_tax"])

@router.post("/", status_code=status.HTTP_201_CREATED)
def create(request:schemas.EmployeeTax, db: Session = Depends(get_db)):
    return employee_tax_repository.create_employee_tax(request, db)


@router.get('/')
def get_members(db:Session=Depends(get_db)):
   return  employee_tax_repository.get_all_employee_tax(db)


@router.get("/{id}", status_code=200)
def show(id, db: Session = Depends(get_db)):
    return employee_tax_repository.get_employee_tax_by_id(id, db)

@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_item(id, request:schemas.EmployeeTax, db: Session = Depends(get_db)):
    return employee_tax_repository.update_employee_tax(id, request, db)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(id, db: Session = Depends(get_db)):
    return employee_tax_repository.delete_employee_tax(id, db)