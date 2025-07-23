# data logic like loading from db
# TODO: (RESEARCH LATER) tbh, not entirely sure if service is where this logic goes? makes sense tho but havent before
# should clean up for cleaner AWS migration replacement too
# Ig it makes sense that i put this in the service module since the SERVICE module handles logic, as practiced at work ... 

from pathlib import Path
import json
# from data.temp_fruit_db import TEMP_DB (only valid for py files ig?)


TEMP_DB_PATH = Path("./data/temp_fruit_db.json")
# TEMP_DB_PATH = Path(__file__).parent.parent / "data" / "temp_fruit_db.json"

def load_temp_db():
    with open(TEMP_DB_PATH, "r") as f:
        return json.load(f)

# TODO: NEED TO FIX, not adding to db
def save_fruit_db(data):
    with open(TEMP_DB_PATH, "w") as f:
        json.dump(data, f, indent=2)