
from fastapi import HTTPException, Response,status
from sqlalchemy.orm import Session
from schema_models import schemas
from database_model import models

def create_membership_plan(request: schemas.MembershipPlanModel, db: Session):
    new_membership_plan = models.MembershipPlan(
        name=request.name,
        price=request.price,
        duration=request.duration
    )
    
    # for role_data in request.roles:
    #     role = db.query(models.Role).filter(models.Role.role_name == role_data.role_name).first()
    #     if role:
    #         new_user.assigned_roles.append(role)
    
    db.add(new_membership_plan)
    db.commit()
    db.refresh(new_membership_plan)
    return new_membership_plan

def get_all_membership_plans(db:Session):
    membership_plans = db.query(models.MembershipPlan).all()
    # user_models = []
    # for user in users:
    #     user_model = schemas.UserModel(
    #         username=user.username,
    #         password=user.password,
    #         status=user.status,
    #         roles=[schemas.RoleModel(role_name=role.role_name, description=role.description) for role in user.assigned_roles]
    #     )
    #     user_models.append(user_model)
    return membership_plans

# def get_membership_plan_by_id(id:int,db:Session):
#     member_data=db.query(models.MembershipPlan).filter(models.MembershipPlan.id==id)
#     if not member_data.first():
#            raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"the membership plan  with id {id} is not available",
#         )
#     return member_data

def get_single_membership_plan(id:int, db:Session):
    data = db.query(models.MembershipPlan).filter(models.MembershipPlan.id == id).first()
    if not data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"the membership plan  with id {id} is not available",
        )
    
    return data

def update_membership_plan(id:int,request: schemas.MembershipPlanModel,db:Session):
    user = db.query(models.MembershipPlan).filter(models.MembershipPlan.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"membership plan   with the id  {id} is not avaialable",
        )
    user.update(request.dict())
    db.commit()
    return "Updated successfully"




def delete_membership_plan(id, db:Session):
    user = db.query(models.MembershipPlan).filter(models.MembershipPlan.id == id)
    if not user.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"membership plan with the id  {id} is not avaialable in the database",
        )
    user.delete(synchronize_session=False)
    db.commit()
    return user


def  get_these():
    return {"detail":"Gashaw Gedef"}