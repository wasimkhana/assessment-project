from typing import List, Optional
from fastapi import APIRouter, Depends, status, HTTPException, Response, Query
from .. import schemas, database, models, oauth2
from sqlalchemy.orm import Session
from ..repository import item

router = APIRouter(
    prefix="/items",
    tags=['Item']
)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_item(request: schemas.Item, db: Session = Depends(database.get_db),
                current_user: schemas.User = Depends(oauth2.get_current_user)):
    """
    Endpoint for creating post of found item.
    Args:
    request: schema of Item table
    db: database connection session
    current_user: login user detail
    """
    return item.create_item(request, db, current_user)


@router.get('/{item_name},{location}', status_code=200)
def get_items(item_name: Optional[str], location: Optional[str], db: Session = Depends(database.get_db),
             current_user: schemas.User = Depends(oauth2.get_current_user)):
    """
    Endpoint for retriving item detials.
    
    Args:
    location: location where item lost/found
    item_name: lost item_name
    db: database connection session
    current_user: login user
    """
    return item.get_items(item_name, location, db)
