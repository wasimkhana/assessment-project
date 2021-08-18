from typing import Optional
from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException, status, Query


def create_item(request: schemas.Item, db: Session, current_user):
    """
    Create item tuple with defined schema in db.
    
    Args:
    request: schema (structure) of item table
    db: database connection session
    current_user: signed-in user email address
    """
    # get current_user details
    current_user_data = db.query(models.User).filter(models.User.email == current_user.email).first()

    # item_name and item_location are converted to lowerCase to keep it safe while retrieving
    new_item = models.Item(item_name=request.item_name.lower(), item_location=request.item_location.lower(),
                           item_description=request.item_description,
                           item_image=request.item_image, user_id=current_user_data.id)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return "Item successfully posted."


def get_items(item_name: Optional[str], location: Optional[str], db: Session):
    """
    Create item tuple with defined schema in db.
    
    Args:
    request: schema (structure) of item table
    db: database connection session
    current_user: signed-in user email address
    
    Errors:
    raiseError: if user email registered
    """

    if location and item_name:
        items = db.query(models.Item).filter(models.Item.item_location == location.lower(),
                                             models.Item.item_name == item_name.lower()).all()

        return [{"item_name": item.item_name, "location": item.item_location,
                 "Description": item.item_description, "item_image": item.item_image} for item in items]


def item_not_found():
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Item with not found')


def update_item(item_id: int, request: schemas.Item, db: Session, current_user):
    current_user_data = db.query(models.User).filter(models.User.email == current_user.email).first()
    item_to_update = db.query(models.Item).filter(models.Item.id == item_id,
                                                  models.Item.user_id == current_user_data.id)
    if not item_to_update.first():
        raise item_not_found()

    item_to_update.update(request.dict())
    db.commit()
    return "Item updated successfully"


def delete_item(item_id: int, db: Session, current_user):
    current_user_data = db.query(models.User).filter(models.User.email == current_user.email).first()
    item_to_delete = db.query(models.Item).filter(models.Item.id == item_id,
                                                  models.Item.user_id == current_user_data.id)

    if not item_to_delete.first():
        raise item_not_found()

    item_to_delete.delete(synchronize_session=False)
    db.commit()
    return "Post successfully deleted"
