from typing import List
from fastapi import APIRouter, Depends, status, HTTPException, Response
from .. import schemas, database, models
from sqlalchemy.orm import Session
from ..repository import user


# A REST API provides mechanism for routing API requests with supporting parameters
router = APIRouter(
    prefix="/user",
    tags=['SignUp']
)



@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.User, db: Session = Depends(database.get_db)):
    """
    Endpoint for creating user.
    Args:
    request: schema of user table
    db: database connection session
    """
    return user.create(request, db)


