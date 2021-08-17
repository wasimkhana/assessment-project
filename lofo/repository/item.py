from typing import Optional
from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException, status, Query


def create_post(request: schemas.Item, db: Session, current_user):
    """
    Create item tuple with defined schema in db.
    
    Args:
    request: schema (structure) of item table
    db: database connection session
    current_user: signed-in user email address
    """
    #get current_user details
    current_user_id = db.query(models.User).filter(models.User.email == current_user.email).first()
    
    #itemname and item_location are converted to lowerCase to keep it safe while retrieving
    new_post = models.Item(itemname = request.itemname.lower(), item_location = request.item_location.lower(), item_description = request.item_description,
    item_image = request.item_image,user_id=current_user_id.id)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post
  
    
def get_posts(itemname: Optional[str], location: Optional[str], db: Session):
    """
    Create item tuple with defined schema in db.
    
    Args:
    request: schema (structure) of item table
    db: database connection session
    current_user: signed-in user email address
    
    Errors:
    raiseError: if user email registered
    """
    print(location, itemname)
    if location and itemname:
        posts = db.query(models.Item).filter(models.Item.item_location == location.lower(), models.Item.itemname== itemname.lower()).first()
        return posts

