# data logic like loading from db, db persistance, etc
# This is where you interact with your database (TODO: RESEARCH: i think this is the ONLY file that should directly touch the database  ??? right ???)


# TODO: (RESEARCH LATER) tbh, not entirely sure if service is where this logic goes? makes sense tho but havent before
# should clean up for cleaner AWS migration replacement too
# Ig it makes sense that i put this in the service module since the SERVICE module handles logic, as practiced at work ... 

from pathlib import Path
import json
from models.fruit_models import FruitModel #TODO: FIX: is it models or schemas ???? I mean ig models is the JSON, not pydantic model, so makes sense ...? Since the schema-models conversion probably doesnt happen here...??


TEMP_DB_PATH = Path("./data/temp_fruit_db.json")
# TEMP_DB_PATH = Path(__file__).parent.parent / "data" / "temp_fruit_db.json"



# POST fixing models x schemas x service layers --------------------------
def load_temp_db():
    # load fruits from db
    with open(TEMP_DB_PATH, "r") as f:
        data = json.load(f)
        return [FruitModel(**fruit) for fruit in data["fruits"]] #TODO: RESEARCH: no idea if this is right
    # with open(TEMP_DB_PATH, "r") as f:
    #     return json.load(f)

# TODO: NEED TO FIX, not adding to db
def save_fruit_db(fruits: list[FruitModel]):
    with open(TEMP_DB_PATH, "w") as f:
        json.dump({"fruits": [fruit.to_dict() for fruit in fruits]}, f, indent=2) #TODO: RESEARCH: so i think that the to_dict() method i implemented successfully replace the .model_dump() method? What are the benefits of using one method over the other? i'm guessing my to_dict() method is better but idk how and why
    
# def save_fruit_db(fruit_models):
#     with open(TEMP_DB_PATH, "w") as f:
#         json.dump({"fruits": [fruit.model_dump() for fruit in fruit_models]}, f, indent=2)  #TODO: FIX: no idea if this is right
#     # with open(TEMP_DB_PATH, "w") as f:
#     #     json.dump(data, f, indent=2)










# # PRE fixing models x schemas x service layers [OLD, WILL BE TRASHED] --------------------------

# def load_temp_db():
#     with open(TEMP_DB_PATH, "r") as f:
#         return json.load(f)

# # TODO: NEED TO FIX, not adding to db
# def save_fruit_db(data):
#     with open(TEMP_DB_PATH, "w") as f:
#         json.dump(data, f, indent=2)