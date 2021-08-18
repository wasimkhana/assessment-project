from typing import Optional
from sqlalchemy.orm import Session
from lofo import models, schemas
from fastapi import HTTPException, status, Query
from lofo.hashing import Hash


def get_user_items(db: Session, current_user):
    """
    Create item tuple with defined schema in db.

    Args:
    request: schema (structure) of item table
    db: database connection session
    current_user: signed-in user email address

    Errors:
    raiseError: if user email registered
    """
    current_user_data = db.query(models.User).filter(models.User.email == current_user.email).first()
    items = db.query(models.Item).filter(models.Item.user_id == current_user_data.id).all()
    return [{"item_name": item.item_name, "location": item.item_location,
             "Description": item.item_description, "item_image": item.item_image} for item in items]


def modify_userprofile(request: schemas.UserInfo, db: Session, current_user):
    user_data_to_change = db.query(models.User).filter(models.User.email == current_user.email)
    request.password = Hash.bcrypt(request.password)
    user_data_to_change.update(request.dict())
    db.commit()
    return "User profile modified"
