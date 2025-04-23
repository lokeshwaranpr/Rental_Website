from jose import JWTError,jwt
from datetime import datetime, timedelta



SECRET_KEY="6385b0948e60616873c9bb5407f6c3a8b67d4f91af73c3fce2c3748e077f2014"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=30

def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm = ALGORITHM)

    return encoded_jwt

