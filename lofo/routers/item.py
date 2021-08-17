from typing import List, Optional
from fastapi import APIRouter, Depends, status, HTTPException, Response, Query
from .. import schemas, database, models,  oauth2
from sqlalchemy.orm import Session
from ..repository import item

router = APIRouter(
    prefix="/item",
    tags=['Posts']
)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Item, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    """
    Endpoint for creating post of found item.
    Args:
    request: schema of Item table
    db: database connection session
    current_user: login user detail
    """
    return item.create_post(request, db, current_user)


@router.get('/posts/{itemname},{location}', status_code= 200)
def get_post(itemname: Optional[str], location: Optional[str], db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    """
    Endpoint for retriving posts detials.
    
    Args:
    location: location where item lost/found
    itemname: lost itemname
    db: database connection session
    current_user: login user
    """
    print(itemname, location)
    return item.get_posts(itemname,location, db)
    
