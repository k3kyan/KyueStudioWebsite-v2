# logic
from fastapi import Depends, status, HTTPException
from models.login_models import Login
# TODO: also import models and database ?? idk, didnt fully follow Ashutosh Pawar's Udemy course so idk, might be important for AWS..?
# from passlib.context import CryptContext # TODO: to decode hashed password and compare it with the password from request // which is not coded yet so prob dont need this now
# actually i wont need to hash or decrypt a password bc it'll be handled elsewhere outside of local, so just use substitute data for now ig


def get_user_from_db(request: Login):
    # TODO: replace with logic to get info from actual database once hooked up to aws
    username = "tempUsername"
    # TODO?: potentially decrypt the password if i do that in the future
    # pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    password = "tempPassword" #would use the password from queried usernameOfficial model object, but i only have one admin on this site so
    
    # if username doesnt exist, return an exception
    if request.username != username:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Username not found / Username invalid")
    
    # TEMP, should be replaced with [*] method if password is wrong, return an exception
    if request.password != password:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect password")
    
    # [*] method that should replace above method, if i use encryption 
    # if decrypted password is wrong, return exception
    # if not pwd_context.verify(request.password, password):
    #     raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect password")
    
    
    # if both of the above methods pass, and both username and password are valid
    # then we generate JWT token
    # Refresher of JWT Token purpose: once user is logged in, JWT token allows them to access the different allowed routes in the API
    # With a JWT Token, we are now able to decide which routes can be protected or public
    # JWT Tokens authorize users to access special protected routes
    # TODO: Generate JWT Token (kinda complicated so i guess i'll do it tomorrow)
    
    