from pydantic import BaseModel
from typing import List, Optional


class User( BaseModel):
    """
    User schema for interaction with API and format retrieving data in JSON.
    
    Args:
    BaseModel: parent class
    """
    
    Fname: str
    Mname: str
    Lname: str
    username: str
    email: str
    profile_image: str
    password: str
    
    
class Item(BaseModel):
    """
    Item schema for interaction with API and format retrieving data in JSON.
    user()
  
    Args:
    BaseModel (class): parent class
    """
    itemname: str
    item_location: str
    item_description: str
    item_image: str

class Login(BaseModel):
    email: str
    password:str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str
