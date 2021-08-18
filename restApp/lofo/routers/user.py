from typing import List
from fastapi import APIRouter, Depends, status, HTTPException, Response
from lofo import schemas, database, models, oauth2
from sqlalchemy.orm import Session
from lofo.repository import user

# A REST API provides mechanism for routing API requests with supporting parameters
router = APIRouter(
    prefix="/user",
    tags=['User']
)


@router.get('/items', status_code=200)
def get_user_items(db: Session = Depends(database.get_db),
                   current_user: schemas.User = Depends(oauth2.get_current_user)):
    """
    Endpoint to retrieve the logged-in user posted items detail.
    """
    return user.get_user_items(db, current_user)


@router.put('/profile', status_code=status.HTTP_202_ACCEPTED)
def modify_userprofile(request: schemas.UserInfo, db: Session = Depends(database.get_db),
                       current_user: schemas.User = Depends(oauth2.get_current_user)):
    """
    Endpoint to modify own(user) profile.
    """
    return user.modify_userprofile(request, db, current_user)
