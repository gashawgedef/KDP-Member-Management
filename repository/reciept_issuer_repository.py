
from fastapi import HTTPException, Response,status
from sqlalchemy.orm import Session
from schema_models import schemas
from database_model import models


def create_reciept_issuers(request: schemas.RecieptIssuerModel,db:Session):
    new_reciept_issuer=models.RecieptIssuer(
        first_name=request.first_name,
        middle_name=request.middle_name,
        last_name=request.last_name,
        gender=request.gender,
        phone=request.phone,
        place_region=request.place_region,
        place_zone=request.place_zone,
        place_wereda=request.place_wereda,
        place_kebele=request.place_kebele
        )
    db.add(new_reciept_issuer)
    db.commit()
    db.refresh(new_reciept_issuer)
    return new_reciept_issuer

def get_all_reciept_issuers(db:Session):
    reciept_issuers=db.query(models.RecieptIssuer).all()
    return reciept_issuers

def get_reciept_issuers_by_id(id:int,db:Session):
    reciept_issuer=db.query(models.RecieptIssuer).filter(models.RecieptIssuer.id==id)
    if not reciept_issuer.first():
           raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"the blog with id {id} is not available",
        )
    return reciept_issuer

def get_single_reciept_issuers(id:int, db:Session):
    reciept_issuer = db.query(models.RecieptIssuer).filter(models.RecieptIssuer.id == id).first()
    if not reciept_issuer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"the blog with id {id} is not available",
        )
        # response.status_code=status.HTTP_404_NOT_FOUND
        return {"detail": f"blog with the id  {id} is not avaialable"}
    return reciept_issuer

def update_reciept_issuers(id:int,request: schemas.RecieptIssuerModel,db:Session):
    reciept_issuer = db.query(models.RecieptIssuer).filter(models.RecieptIssuer.id == id)
    if not reciept_issuer.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"blog with the id  {id} is not avaialable",
        )
    reciept_issuer.update(request.dict())
    db.commit()
    return "Updated successfully"




def delete_reciept_issuers(id, db:Session):
    reciept_issuer = db.query(models.RecieptIssuer).filter(models.RecieptIssuer.id == id)
    if not reciept_issuer.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"blog with the id  {id} is not avaialable in the database",
        )
    reciept_issuer.delete(synchronize_session=False)
    db.commit()
    return reciept_issuer

