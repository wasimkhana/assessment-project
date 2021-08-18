from pydantic import BaseModel
from typing import List, Optional


# schema to add User detail
class User(BaseModel):
    """
    User schema for interaction with API and format retrieving data in JSON.
    
    Args:
    BaseModel: parent class
    """

    firstname: str
    middlename: str
    lastname: str
    username: str
    email: str
    profile_image: str
    password: str


class UserInfo(BaseModel):
    firstname: str
    middlename: str
    lastname: str
    profile_image: str
    password: str


# schema to add Item details
class Item(BaseModel):
    """
    Item schema for interaction with API and format retrieving data in JSON.
    
  
    Args:
    BaseModel (class): parent class
    """
    item_name: str
    item_location: str
    item_description: str
    item_image: str


# schema to add login details
class Login(BaseModel):
    email: str
    password: str


# schema to hold token details
class Token(BaseModel):
    access_token: str
    token_type: str


# schema to hold login_user email-address
class TokenData(BaseModel):
    email: str
