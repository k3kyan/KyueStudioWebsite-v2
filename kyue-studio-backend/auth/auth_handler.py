from fastapi import HTTPException, status, APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm #TODO: RESEARCH: what is OAuth2PasswordRequestForm??
from typing import Optional
from datetime import datetime, timedelta, timezone
from jose import jwt
import os
# Purpose of this file: generate jwt token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token") # endpoint for token retrieval // this says "this tokenUrl will be required to receive token for our schema"

# SECRET_KEY = "725898e2e6208a094e60f59ebf97b32940f4902b1ffe606be5f67dc89cf74ee0" #randomly generated string using command "openssl rand -hex 32"
# ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Generates JWT Token
# From Catalan Stefan and Tech w Tim and Ashutosh Pawar
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    SECRET_KEY = os.getenv("SECRET_KEY")
    ALGORITHM = os.getenv("ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")

    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt




# TODO: LATER: i'm going to implement the security and encryption stuff later bc idk how it will work w AWS

# TODO: ? METHODS FOR LATER POTENTIALLY ----------------------------------------------------------------

# router = APIRouter(
#     # prefix="/auth",
#     # tags=["auth"],
#     # responses={404: {"description": "Not found"}}
# )


# def verify_password(plain_password, hashed_password):
#     return plain_password == hashed_password

# ?? i think i already implemented this as "get_token" in authentication_routes.py (jk i also called it authenticate_user in authentication_routes.py)
# def authenticate_user(username: str, password: str):
#     user = get_user_from_db(username)
#     if not user:
#         return False
#     if not verify_password(password, user.hashed_password):
#         return False
#     return user


# prob would only need if i'm implementing multiple users
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