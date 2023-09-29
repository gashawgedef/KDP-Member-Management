


from pydantic import BaseModel


class Members(BaseModel):
    first_name:str
    last_name:str
    phone:str
    email:str