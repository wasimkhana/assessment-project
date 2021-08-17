from pydantic import BaseModel
from typing import List, Optional

#schema to add User detail
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
    
#schema to add Item details
class Item(BaseModel):
    """
    Item schema for interaction with API and format retrieving data in JSON.
    
  
    Args:
    BaseModel (class): parent class
    """
    itemname: str
    item_location: str
    item_description: str
    item_image: str


#schema to get Item details  
class UpdateItem(BaseModel):
    """
    Item schema to get items details.
  
    Args:
    BaseModel (class): parent class
    """
    itemname: str
    item_location: str
    item_description: str
    date_posted: str
    item_image: str


#schema to add login details
class Login(BaseModel):
    email: str
    password:str

#schema to hold token details
class Token(BaseModel):
    access_token: str
    token_type: str

#schema to hold login_user email-address
class TokenData(BaseModel):
    email: str
