
from fastapi import HTTPException, Response,status
from sqlalchemy.orm import Session
from schema_models import schemas
from database_model import models
from .hashing import Hash
def create_employee_tax(request: schemas.EmployeeTax,db:Session):
    new_member=models.EmployeeTax(
        employee_name=request.employee_name,tin_no=request.tin_no,basic_salary=request.basic_salary,transport_allowance=request.transport_allowance,
        additional_benefits=request.additional_benefits,taxable_income=request.taxable_income,tax_with_hold=request.tax_with_hold,net_pay=request.net_pay,
        brance_name=Hash.bcrypt(request.brance_name)
        )
    db.add(new_member)
    db.commit()
    db.refresh(new_member)
    return new_member

def get_all_employee_tax(db:Session):
    members=db.query(models.EmployeeTax).all()
    return members

def get_employee_tax_by_id(id:int,db:Session):
    member_data=db.query(models.EmployeeTax).filter(models.EmployeeTax.id==id)
    if not member_data.first():
           raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"the employee tax with id {id} is not available",
        )
    return member_data

def get_single_employee_tax(id:int, db:Session):
    data = db.query(models.EmployeeTax).filter(models.EmployeeTax.id == id).first()
    if not data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"the blog with id {id} is not available",
        )
        # response.status_code=status.HTTP_404_NOT_FOUND
        return {"detail": f"blog with the id  {id} is not avaialable"}
    return data

def update_employee_tax(id:int,request: schemas.EmployeeTax,db:Session):
    blog = db.query(models.EmployeeTax).filter(models.EmployeeTax.id == id)
    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"blog with the id  {id} is not avaialable",
        )
    blog.update(request.dict())
    db.commit()
    return "Updated successfully"




def delete_employee_tax(id, db:Session):
    blog = db.query(models.EmployeeTax).filter(models.EmployeeTax.id == id)
    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"blog with the id  {id} is not avaialable in the database",
        )
    blog.delete(synchronize_session=False)
    db.commit()
    return blog


def  get_these():
    return {"detail":"Gashaw Gedef"}