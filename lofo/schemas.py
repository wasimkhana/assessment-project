from pydantic import BaseModel
from typing import List, Optional


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
    

class Login(BaseModel):
    email: str
    password:str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
