from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm 
from auth import auth_handler

authentication_router = APIRouter(
    # prefix="/auth",
    tags=["authentication"],
    # responses={404: {"description": "Not found"}}
)

# Creating the /token endpoint from auth_handler.py (oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token"))
# TODO: LATER: will need another depends parameter for getting user and verifying that password is correct (tho idk how that works with aws secrets manager ???)
@authentication_router.post("/token")
def authenticate_user(request: OAuth2PasswordRequestForm = Depends()): #db: Session = Depends(get_db))
    # TODO: TEMP:  Get user from db (idk if this applies to me)
    username = "tempUsername" # TODO: replace with: username = query from db
    # if invalid username
    if request.username != username:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")
    
    # TODO: TEMP: Check if password of the user is correct
    password = "tempPassword" # TODO: replace with: password = query from db / from the found username ???
    if request.password != password: #did not decrypt/verify/hash/etc like in Catalin Stefan's tutorial
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")
    
    access_token = auth_handler.create_access_token(data={"sub": request.username}) # TODO: FIX: ??  not sure if "request.username" is correct // i think it should just be my username from AWS ?? the single one, not necessarily the one passed in, but ig if its reached that line then its correct/the same...?
    
    return {
        "access_token": access_token, 
        "token_type": "bearer"
        # "username": request.username
        # "user_id": ?? idk just whatever other data i'd wanna return , idk why i would tho but Catalin Stefan did it, i wont for now tho
        }