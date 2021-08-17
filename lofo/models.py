from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class User( Base):
    """
    Model to interact with `User` table through following structure
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
    profile_image =  Column( String(40), default='default.jpg')
    password =  Column( String, nullable=False)
    
    finder = relationship("Item")
   
class Item(Base):
    """
    Model to interact with `Item` through following structure
    user()
  
    Args:
    Base (class): parent class
    """
    __tablename__ = "posts"
    id = Column( Integer, primary_key=True, index=True)
    itemname = Column( String(40), nullable=False)
    item_location = Column( String(120), nullable=False)
    item_description = Column( String, nullable=False)
    date_posted = Column( DateTime, nullable=False, default=datetime.utcnow)
    item_image =  Column( String(40))
    user_id = Column( Integer,  ForeignKey('users.id'), nullable=False)
    
