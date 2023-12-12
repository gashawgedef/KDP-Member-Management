from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from  database_connection import get_db
from schema_models import schemas
from repository import membership_plan_repository


router = APIRouter(prefix="/membership_plans", tags=["membership_plans"])

@router.post("/", status_code=status.HTTP_201_CREATED)
def create(request:schemas.MembershipPlanModel, db: Session = Depends(get_db)):
    return membership_plan_repository.create_membership_plan(request, db)


@router.get('/')
def get_membershin_plans(db:Session=Depends(get_db)):
   return  membership_plan_repository.get_all_membership_plans(db)


@router.get("/{id}", status_code=200)
def show_single_membership(id, db: Session = Depends(get_db)):
    return membership_plan_repository.get_single_membership_plan(id, db)

@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_membership_plan(id, request:schemas.MembershipPlanModel, db: Session = Depends(get_db)):
    return membership_plan_repository.update_membership_plan(id, request, db)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_membership_plan(id, db: Session = Depends(get_db)):
    return membership_plan_repository.delete_membership_plan(id, db)