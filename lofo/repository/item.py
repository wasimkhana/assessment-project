from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException, status


def create_post(request: schemas.Item, db: Session, current_user):
    """
    Create item tuple with defined schema in db.
    
    Args:
    request: schema (structure) of item table
    db: database connection session
    current_user: signed-in user email address
    
    Errors:
    raiseError: if user email registered
    """
    #get current_user details
    current_user_id = db.query(models.User).filter(models.User.email == current_user.email).first()
    new_post = models.Item(itemname = request.itemname, item_location = request.item_location, item_description = request.item_description,
    item_image = request.item_image,user_id=current_user_id.id)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post
