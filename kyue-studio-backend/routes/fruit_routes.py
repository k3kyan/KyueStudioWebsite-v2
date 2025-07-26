# TEMP: endpoint logic
# i think its more common to use the term "routes" than "endpoints" ? in projects
# TODO: future files: auth_routes.py, blog_routes.py, cart_routes.py, order_routes.py, product_routes.py, etc
# TODO: This file should just be for endpoints/routes, not logic. 
#       Calculate data manipulation logic from another file and import those methods into these route methods. Cleaner, modular

from fastapi import APIRouter
# from models.fruit_models import Fruit, Fruits
from auth.auth_handler import oauth2_scheme #For Auth
from fastapi import Depends #For Auth

from models.fruit_models import FruitModel #JSON models
from schemas.fruit_schema import FruitSchema, FruitsSchema #Pydantic schemas
from services.fruit_service import load_temp_db, save_fruit_db

# this router will get added to the main FastAPI app!!
fruit_router = APIRouter(
    # TODO: customize these fields later
    # prefix="/fruits",
    tags=["fruits"]
    # responses={404: {"description": "Not found"}}
)


# GET
# returns data in the format model of class Fruits
@fruit_router.get("/fruits", response_model=list[FruitSchema])
def get_fruits():
    return [model.to_schema() for model in load_temp_db()] # ??? idk if this is right 
    # data = load_temp_db()
    # return Fruits(fruits=data["fruits"])

# POST
# adds a new fruit
# TODO: make protected route / secure the endpoint
@fruit_router.post("/fruits", response_model=FruitSchema)
def add_fruit(fruit: FruitSchema, token: str = Depends(oauth2_scheme)): # oh, all i needed to do to secure the endpoint was add the this "token: str = Depends(oauth2_scheme)" parameter in the endpoint method. p cool!!
    fruits = load_temp_db()
    fruits.append(FruitModel.from_schema(fruit))
    save_fruit_db(fruits)
    return fruit
    # data = load_temp_db()
    # data["fruits"].append(fruit.model_dump()) # NECESSARY FOR SAVING TO JSON!! Needs to convert to json format, or else errors. .model_dump() = .dict()
    # save_fruit_db(data)
    # return fruit