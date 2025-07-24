# - generate jwt token
# - 

# TODO: LATER: i'm going to implement the security and encryption stuff later bc idk how it will work w AWS

import jwt #not installed ????
from fastapi import HTTPException, status, APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm #TODO: RESEARCH: what is OAuth2PasswordRequestForm??
from typing import Optional
from datetime import datetime, timedelta
# from jose import jwt # ??????

# endpoint for token retrieval
# this says "this tokenUrl will be required to receive token for our schema"
# TODO: create this endpoint
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

SECRET_KEY = "725898e2e6208a094e60f59ebf97b32940f4902b1ffe606be5f67dc89cf74ee0" #randomly generated string using command "openssl rand -hex 32"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30



router = APIRouter(
    # prefix="/auth",
    # tags=["auth"],
    # responses={404: {"description": "Not found"}}
)

# def verify_password(plain_password, hashed_password):
#     return plain_password == hashed_password

# def authenticate_user(username: str, password: str):
#     user = get_user_from_db(username)
#     if not user:
#         return False
#     if not verify_password(password, user.hashed_password):
#         return False
#     return user


# From Catalan Stefan and Tech w Tim
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# async def get_current_user(token: str = Depends(oauth2_scheme)):
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         username: str = payload.get("sub")
#         if username is None:
#             raise credentials_exception
#         token_data = TokenData(username=username)
#     except JWTError:
#         raise credentials_exception