
from fastapi import HTTPException, Response,status
from sqlalchemy.orm import Session
from schema_models import schemas
from database_model import models


def create_reciept_items(request: schemas.RecieptItemsModel,db:Session):
    new_reciept_items=models.RecieptItems(
        receipt_issuer_id=request.receipt_issuer_id,
        identifier=request.identifier,
        from_number=request.from_number,
        to_number=request.to_number,
        date_taken=request.date_taken,
        return_date=request.return_date,
        amount_birr=request.amount_birr
        )
    db.add(new_reciept_items)
    db.commit()
    db.refresh(new_reciept_items)
    return new_reciept_items

def get_all_reciept_items(db:Session):
    reciept_items=db.query(models.RecieptItems).all()
    return reciept_items



def get_single_reciept_item(id:int, db:Session):
    reciept_items = db.query(models.RecieptItems).filter(models.RecieptItems.id == id).first()
    if not reciept_items:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"the blog with id {id} is not available",
        )
        # response.status_code=status.HTTP_404_NOT_FOUND
        return {"detail": f"blog with the id  {id} is not avaialable"}
    return reciept_items

def update_reciept_item(id:int,request: schemas.RecieptItemsModel,db:Session):
    reciept_items = db.query(models.RecieptItems).filter(models.RecieptItems.id == id)
    if not reciept_items.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"receipt item with with the id  {id} is not avaialable",
        )
    reciept_items.update(request.dict())
    db.commit()
    return "Updated successfully"




def delete_reciept_item(id, db:Session):
    reciept_items = db.query(models.RecieptItems).filter(models.RecieptItems.id == id)
    if not reciept_items.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Receipt item  with the id  {id} is not avaialable in the database",
        )
    reciept_items.delete(synchronize_session=False)
    db.commit()
    return reciept_items

