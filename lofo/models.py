from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class User( Base):
    """
    Model to interact with `User` table with a structure
    user(id, Fname, Mname, Lname, username, email, profile_image, password)
  
    Args:
    Base (class): parent class
    """
    __tablename__ = "users"
    
    # last login, login location can be used for security as per need
    id =  Column( Integer, primary_key=True)
    Fname = Column( String(20), nullable=False)
    Mname = Column( String(20), nullable=True)
    Lname = Column( String(20), nullable=True)
    username =  Column( String(20), unique=True, nullable=False)
    email =  Column( String(80), unique=True, nullable=False)
    profile_image =  Column( String(20), default='default.jpg')
    password =  Column( String(60), nullable=False)
