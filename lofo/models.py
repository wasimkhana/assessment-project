from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base


class User(Base):
    """
    Model for `user` table will have following structure
    user(id, firstname, middlename, lastname, username, email, profile_image, password)
  
    Args:
    Base (class): parent class
    """
    __tablename__ = "user"

    # last login, login location can be used for security as per need
    id = Column(Integer, primary_key=True)
    firstname = Column(String(20), nullable=False)
    middlename = Column(String(20), nullable=True)
    lastname = Column(String(20), nullable=True)
    username = Column(String(20), unique=True, nullable=False)
    email = Column(String(80), unique=True, nullable=False)
    profile_image = Column(String(40), default='default.jpg')
    password = Column(String, nullable=False)

    finder = relationship("Item")


class Item(Base):
    """
    Model for `item` table will have following structure
    item(id, item_name, item_location, item_description, creation_date, email, item_image, user_id)
  
    Args:
    Base (class): parent class
    """
    __tablename__ = "item"
    id = Column(Integer, primary_key=True, index=True)
    item_name = Column(String(40), nullable=False)
    item_location = Column(String(120), nullable=False)
    item_description = Column(String, nullable=False)
    creation_date = Column(DateTime, nullable=False, default=datetime.utcnow)
    item_image = Column(String(40))
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
