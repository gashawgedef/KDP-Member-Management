

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