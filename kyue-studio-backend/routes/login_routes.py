from fastapi import APIRouter
from models.login_models import Login
# from services.fruit_service import load_temp_db, save_fruit_db
from services.login_service import get_user_from_db

# instance of APIRouter
login_router = APIRouter(
    # prefix="/login",
    # tags=["login"],
    # responses={404: {"description": "Not found"}}
)

@login_router.post("/login")
def login(request: Login):
    get_user_from_db(request)
    return {"TEMP: correct login info"}

# TODO: endpoint for logging out. only shows up when logged in. 

# @login_router.post("/token")
# async def login_for_access_token(form_data: ):
# idk, see tech w tim, but this is used for getting a token once you successfully login and authenticate the user i think ... ?? 
# Then u run the create_access_token() method, and return the token, so now the user has a token to use to access the API


# # Protected route?!!?!
# # see Tech w Tim github/tutorial
# It is this parameter that protects the route ?!?!! : current_user: User = Depends(get_current_active_user)
# @login_router.get("/users/me", response_model=UserResponse)
# async def read_users_me(current_user: User = Depends(get_current_active_user)):
#     return current_user