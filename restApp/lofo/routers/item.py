from typing import List, Optional
from fastapi import APIRouter, Depends, status, HTTPException, Response, Query
from lofo import schemas, database, models, oauth2
from sqlalchemy.orm import Session
from lofo.repository import item

router = APIRouter(
    prefix="/items",
    tags=['Item']
)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_item(request: schemas.Item, db: Session = Depends(database.get_db),
                current_user: schemas.User = Depends(oauth2.get_current_user)):
    """
    Endpoint to create found item (mean post found item).
    """
    return item.create_item(request, db, current_user)


@router.get('/{item_name},{location}', status_code=200)
def get_items(item_name: Optional[str], location: Optional[str], db: Session = Depends(database.get_db),
              current_user: schemas.User = Depends(oauth2.get_current_user)):
    """
    Endpoint for retriving item detials in the specified location with given name.
    """
    return item.get_items(item_name, location, db)


@router.put('/{item_id: int}', status_code=status.HTTP_202_ACCEPTED)
def update_item(item_id: int, request: schemas.Item, db: Session = Depends(database.get_db),
                current_user: schemas.User = Depends(oauth2.get_current_user)):
    """
    Endpoint for to update specific item details posted by the logged-in user.
    """
    return item.update_item(item_id, request, db, current_user)


@router.delete('/{item_id:int}', status_code=status.HTTP_202_ACCEPTED)
def delete_item(item_id: int, db: Session = Depends(database.get_db),
                current_user: schemas.User = Depends(oauth2.get_current_user)):
    """
    Endpoint to delete a specific item (posted by logged-in user) by the user.
    """
    return item.delete_item(item_id, db, current_user)
