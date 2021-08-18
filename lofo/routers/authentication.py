from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from lofo import schemas, database, models, token
from lofo.hashing import Hash
from sqlalchemy.orm import Session

router = APIRouter(tags=['Login'])


@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    """
    Authenticate credentials to generate access_token.
    Args:
    request: login credentials
    db: database connection session
    """
    user = db.query(models.User).filter(
        models.User.email == request.username).first()
    # if email is not correct raise exception
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invalid Credentials")
    # if password is not correct raise exception
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Incorrect password")
    # generated access token
    access_token = token.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
