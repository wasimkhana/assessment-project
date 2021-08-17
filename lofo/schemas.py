from pydantic import BaseModel
from typing import List


class User( BaseModel):
    """
    User schema for interaction with API and format retrieving data in JSON.
    
    Args:
    BaseModel: parent class
    """
    id: int 
    Fname: str
    Mname: str
    Lname: str
    username: str
    email: str
    profile_image: str
    password: str
