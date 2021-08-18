from datetime import datetime, timedelta
from jose import JWTError, jwt
from lofo import schemas

SECRET_KEY = "kwMUB1MCrxs84jUmWhslgYvidxoBBoE4wRINkL-5e6servSA5mrSPnHgGnhnKZLX3S9ZlJqz35ZIs5rkGi7ZVA"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict):
    """
    Creating access token.
    Args:
    data: user credentials
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_token(token: str, credentials_exception):
    """
    To verify token for the user.
    Args:
    token: generated token
    credentials_exception: response
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = schemas.TokenData(email=email)
        return token_data
    except JWTError:
        raise credentials_exception
