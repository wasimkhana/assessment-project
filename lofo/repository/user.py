import re
from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException, status, Response
from ..hashing import Hash


def validate_password(password):
    """
    Password strength is validated.
    
    Args:
    password: entered password for user account
    """
    #if the password has at least 8 character long length and include special character
    #number and alphabets each at least 1
    if not re.findall(r'.*(?=.{8,})(?=.*\d)(?=.*[a-zA-Z])(?=.*[@#$%^&+=]).*$', password):
        return True
    else:
        return False


def validate_email(email):
    """
    Validate an email.
    
    Args:
    emial: entered email for user account.
    """
    #if the password has at least 8 character long length and include special character
    #number and alphabets each at least 1
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
    #validate password strength
    if validate_password(request.password):
        raise HTTPException(status_code = 409, detail = 'Password should include at least 1 alphabet, number and special character and  at least 8 character length')
    
    #validate email   
    if validate_email(request.email):
        raise HTTPException(status_code = 409, detail = 'Please enter valid email-address')
    
    #check if the given email is already registered
    new_user = db.query(models.User).filter(models.User.email == request.email).first()
    if new_user:
        raise HTTPException(status_code = 409, detail = 'An account is already with your email.')
    new_user = models.User(username=request.username,Fname= request.Fname, Mname=request.Mname,
    Lname= request.Lname, email= request.email, profile_image=request.profile_image, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return "Account successfully created"

