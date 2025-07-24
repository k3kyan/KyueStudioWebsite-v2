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