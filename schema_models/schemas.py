

from typing import List, Optional
from pydantic import BaseModel

class Members(BaseModel):
    first_name:str
    middle_name:str
    last_name:str
    phone:str
    email:str
    profession:str
    birth_date:str
    birth_place_region:str
    birth_place_zone:str
    birth_place_wereda:str
    birth_place_kebele:str

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


    
class EmployeeTax(BaseModel):
    
    employee_name:str
    tin_no:int
    basic_salary:float
    transport_allowance:float
    additional_benefits:str
    taxable_income:float
    tax_with_hold:str
    net_pay:float
    brance_name:str


class RoleModel(BaseModel):
    role_name: str
    description: Optional[str] = None

class UserModel(BaseModel):
    username: str
    password: str
    status: str
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


