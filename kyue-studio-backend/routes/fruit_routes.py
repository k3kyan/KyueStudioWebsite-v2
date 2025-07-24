# TEMP: endpoint logic
# i think its more common to use the term "routes" than "endpoints" ? in projects
# TODO: future files: auth_routes.py, blog_routes.py, cart_routes.py, order_routes.py, product_routes.py, etc
# TODO: This file should just be for endpoints/routes, not logic. 
#       Calculate data manipulation logic from another file and import those methods into these route methods. Cleaner, modular

from fastapi import APIRouter
from models.fruit_models import Fruit, Fruits
from services.fruit_service import load_temp_db, save_fruit_db
from auth.auth_handler import oauth2_schema #For Auth
from fastapi import Depends #For Auth

# this router will get added to the main FastAPI app!!
fruit_router = APIRouter(
    # TODO: customize these fields later
    # prefix="/fruits",
    # tags=["fruits"],
    # responses={404: {"description": "Not found"}}
)


# GET
# returns data in the format model of class Fruits
@fruit_router.get("/fruits", response_model=Fruits)
def get_fruits():
    data = load_temp_db()
    return Fruits(fruits=data["fruits"])

# POST
# adds a new fruit
# TODO: make protected route / secure the endpoint
@fruit_router.post("/fruits", response_model=Fruit)
def add_fruit(fruit: Fruit, token: str = Depends(oauth2_schema)): # oh, all i needed to do to secure the endpoint was add the this "token: str = Depends(oauth2_schema)" parameter in the endpoint method. p cool!!
    data = load_temp_db()
    data["fruits"].append(fruit.model_dump()) # NECESSARY FOR SAVING TO JSON!! Needs to convert to json format, or else errors. .model_dump() = .dict()
    save_fruit_db(data)
    return fruit