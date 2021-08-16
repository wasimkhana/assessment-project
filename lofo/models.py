from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class User( Base):
    """
    Model to interact with `User` table.
  
    Args:
    Base (class): parent class
    """
    __tablename__ = "users"
    id =  Column( Integer, primary_key=True)
    username =  Column( String(20), unique=True, nullable=False)
    email =  Column( String(120), unique=True, nullable=False)
    image_file =  Column( String(20), nullable=False, default='default.jpg')
    password =  Column( String(60), nullable=False)
