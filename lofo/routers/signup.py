import re
from typing import List
from fastapi import APIRouter, Depends, status, HTTPException, Response
from .. import schemas, database, models
from sqlalchemy.orm import Session
from ..repository import user
from ..hashing import Hash

# A REST API provides mechanism for routing API requests with supporting parameters
router = APIRouter(
    tags=['SignUp']
)


def validate_password(password):
    """
    Password strength is validated.
    
    Args:
    password: entered password for user account
    """
    # if the password has at least 8 character long length and include special character
    # number and alphabets each at least 1
    if not re.findall(r'.*(?=.{8,})(?=.*\d)(?=.*[a-zA-Z])(?=.*[@#$%^&+=]).*$', password):
        return True
    else:
        return False


def validate_email(email):
    """
    Validate an email.
    
    Args:
    email: entered email for user account.
    """
    # if the password has at least 8 character long length and include special character
    # number and alphabets each at least 1
    if not re.findall(r'^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$', email):
        return True
    else:
        return False


def create_user(request: schemas.User, db: Session):
    """
    Create user tuple with defined schema in db.
    
    Args:
    request: schema (structure) of user table
    db: database connection session
    
    raiseError: if user email registered
    """
    # validate password strength
    if validate_password(request.password):
        raise HTTPException(status_code=409,
                            detail='Password should include at least 1 alphabet, '
                                   'number and special character and  at least 8 character length')

    # validate email
    if validate_email(request.email):
        raise HTTPException(status_code=409, detail='Please enter valid email-address')

    # check if the given email is already registered
    new_user = db.query(models.User).filter(models.User.email == request.email).first()
    if new_user:
        raise HTTPException(status_code=409, detail='An account is already registered with your email.')

    # check if the username is available
    new_user = db.query(models.User).filter(models.User.username == request.username).first()
    if new_user:
        raise HTTPException(status_code=409, detail='username not available')

    new_user = models.User(username=request.username, firstname=request.firstname, middlename=request.middlename,
                           lastname=request.lastname, email=request.email, profile_image=request.profile_image,
                           password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return "Account successfully created"


@router.post('/signup', status_code=status.HTTP_201_CREATED)
def create_user(request: schemas.User, db: Session = Depends(database.get_db)):
    """
    Endpoint to create user-profile. The system uses encryption to keep your password secure.
    """
    return user.create_user(request, db)
