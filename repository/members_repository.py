
from itertools import count
from fastapi import HTTPException, Response,status
from sqlalchemy.orm import Session
from schema_models import schemas
from database_model import models


def create_members(request: schemas.Members,db:Session):
    new_member=models.Member(
        first_name=request.first_name,
        middle_name=request.middle_name,
        last_name=request.last_name,
        gender=request.gender,
        phone=request.phone,
        email=request.email,
        birth_date=request.birth_date,
        birth_place_region=request.birth_place_region,
        birth_place_zone=request.birth_place_zone,
        birth_place_wereda=request.birth_place_wereda,
        birth_place_kebele=request.birth_place_kebele,
        work_place=request.work_place,
        country=request.country,
        address_region=request.address_region,
        address_zone=request.address_zone,
        address_wereda=request.address_wereda,
        payment_status=request.payment_status,
        member_status=request.member_status,
        membership_year=request.membership_year,
        is_staff=request.is_staff
        )
    db.add(new_member)
    db.commit()
    db.refresh(new_member)
    return new_member



def get_all_members(db: Session, pagination_params: schemas.Pagination, first_name: str = None, status: str = None):
    # Apply pagination parameters to the query
    query = db.query(models.Member)

    # Filter by first_name if provided
    if first_name:
        query = query.filter(models.Member.first_name == first_name)

    # Filter by status if provided
    if status:
        query = query.filter(models.Member.member_status == status)
    
    # Count the total number of results without pagination
    total_results = query.count()

    if pagination_params.order == schemas.SortEnum.ASC:
        query = query.order_by(models.Member.id.asc())
    else:
        query = query.order_by(models.Member.id.desc())
    query = query.offset((pagination_params.page - 1) * pagination_params.perPage)
    query = query.limit(pagination_params.perPage)
    
    # Fetch the data
    data = query.all()



    return {"total_results": total_results, "data": data}







def get_member_by_id(id:int,db:Session):
    member_data=db.query(models.Member).filter(models.Member.id==id)
    if not member_data.first():
           raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"the blog with id {id} is not available",
        )
    return member_data

def get_single_member(id:int, db:Session):
    data = db.query(models.Member).filter(models.Member.id == id).first()
    if not data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"the blog with id {id} is not available",
        )
        # response.status_code=status.HTTP_404_NOT_FOUND
        return {"detail": f"blog with the id  {id} is not avaialable"}
    return data

def update_member(id:int,request: schemas.Members,db:Session):
    blog = db.query(models.Member).filter(models.Member.id == id)
    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"blog with the id  {id} is not avaialable",
        )
    blog.update(request.dict())
    db.commit()
    return "Updated successfully"




def delete_member(id, db:Session):
    blog = db.query(models.Member).filter(models.Member.id == id)
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