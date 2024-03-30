

from datetime import date
from enum import Enum
from typing import List, Optional
from fastapi import Query
from pydantic import BaseModel
from sqlalchemy import false

class Members(BaseModel):
    first_name: str
    middle_name: str
    last_name: str
    gender: str
    phone: str
    email: str
    birth_date: str
    birth_place_region:str
    birth_place_zone: str
    birth_place_wereda:str
    birth_place_kebele:str
    work_place: str
    country: str
    address_region: str
    address_zone: str
    address_wereda: str
    payment_status: str  
    member_status : str
    membership_year: date
    is_staff: bool
    
class ProfessionType(BaseModel):
    profession_name:str
    profession_description:str

class MembersAddress(BaseModel):
    name: str
    country: str
    address_region:str
    address_zone: str
    address_wereda: str
    annual_contribution: float
    membership_year:str
    member_id:int


class DanationTypeSchema(BaseModel):
    donation_name:str
    description:str

class AnouncementSchema(BaseModel):
    title:str
    content:str
    posted_date:str

class ProjectSchema(BaseModel):
    project_name:str
    description:str
    start_date:str
    end_date:str
    estimated_budget:str
    status:str




class RoleModel(BaseModel):
    role_name: str
    description: Optional[str] = None

class UserModel(BaseModel):
    username: str
    password: str
    status: bool
    roles: List[RoleModel] = []
    class Config:
        orm_mode = True



class Login(BaseModel):
    username:str
    password:str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None
    id: int | None = None
    status: bool | None = None
    roles: List[dict] = []

class MembershipPlanModel(BaseModel):
    name :str
    price :str
    duration :str


# class RecieptItemsModel(BaseModel):
#     receipt_issuer_id: int
#     identifier: str
#     from_number: str
#     to_number: str
#     date_taken: date
#     return_date: Optional[date] = None
#     amount_birr: float
#     class Config:
#         orm_mode = True

# class RecieptIssuerCreateModel(BaseModel):
#     first_name: str
#     middle_name: str
#     last_name: str
#     gender: str
#     phone: str
#     place_region: str
#     place_zone: str
#     place_wereda: str
#     place_kebele: str


# class RecieptIssuerModel(RecieptIssuerCreateModel):
#     id: int
#     receipt_items: List[RecieptItemsModel] = []

#     class Config:
#         orm_mode = True
class RecieptIssuerBase(BaseModel):
    first_name: str
    middle_name: str
    last_name: str
    gender: str
    phone: str
    place_region: str
    place_zone: str
    place_wereda: str
    place_kebele: str

class RecieptIssuerCreateModel(RecieptIssuerBase):
    pass

class RecieptIssuerModel(RecieptIssuerBase):
    id: int

    class Config:
        orm_mode = True

class RecieptItemsModel(BaseModel):
    identifier: str
    receipt_issuer_id: int
    from_number: str
    to_number: str
    date_taken: date
    return_date: Optional[date] = None
    amount_birr: float
    receipt_issuer: Optional[dict] = None  # To hold the information about the ReceiptIssuer

    class Config:
        orm_mode = True
class SortEnum(Enum):
    ASC="asc"
    DESC="desc"

class Pagination(BaseModel):
      page: int
      perPage: int

def pagination_params(
        page: int = Query(ge=1, required=False, default=1, le=500000),
        perPage: int = Query(ge=1, le=100, required=False, default=10),
        order: SortEnum = SortEnum.DESC
) -> Pagination:
    return Pagination(perPage=perPage, page=page, order=order)
