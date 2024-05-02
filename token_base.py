import jwt
from datetime import datetime, timedelta

SECRECT_KEY = 'HEHUAISEN'
ALGORITHM = 'HS256'
expires_delta = timedelta(minutes=15)

def create_access_token(data: dict, expires_delta: timedelta = expires_delta) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(to_encode, SECRECT_KEY, algorithm=ALGORITHM)
    return encoded_jwt