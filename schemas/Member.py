

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
