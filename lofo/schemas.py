from pydantic import BaseModel
from typing import List


class User( BaseModel):
    """
    User schema for interaction with API and format retrieving data in JSON.
    
    Args:
    BaseModel: parent class
    """
    id: int 
    username: str
    email: str
    image_file: str
    password: str
