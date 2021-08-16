from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException, status, Response

def create(request: schemas.User, db: Session):
    """
    Create user tuple with defined schema in db.
    
    Args:
    request: schema (structure) of user table
    db: database connection session
    
    raiseError: if user email registered
    """
    #check if the given email is already registered
    new_user = db.query(models.User).filter(models.User.email == request.email).first()
    if new_user:
        raise HTTPException(status_code = 409, detail = f'User has already an account')
    new_user = models.User(username=request.username, email= request.email, image_file=request.image_file, password=request.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return "Account successfully created"

