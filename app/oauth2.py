from jose import JWTError,jwt
from datetime import datetime, timedelta
from . import schemas
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')


SECRET_KEY="6385b0948e60616873c9bb5407f6c3a8b67d4f91af73c3fce2c3748e077f2014"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=30

def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm = ALGORITHM)

    return encoded_jwt

def verify_access_token(token: str, credentials_exception):

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id: str = payload.get("user_id")
        if id is None:
            raise credentials_exception
        
        token_data = schemas.TokenData(id=id)

    except JWTError:
        raise credentials_exception
    
    return token_data
    
def get_current_user(token: str = Depends(oauth2_scheme)):
    credential_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Could not validate user credentials", headers={"WWW-Authenticate":"Bearer"})

    return verify_access_token(token, credential_exception)


    