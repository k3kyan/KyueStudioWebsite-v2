from pathlib import Path #temp for json db
import json #temp for json db
from models.contact_form_messages_models import ContactFormMessageModel #no need to import TagsEnum bc it doesnt exist in models, u dont have a separate json file or db for TagsEnum or anything
from schemas.contact_form_messages_schemas import TagEnum #only here for grabbing the tags from schemas.py

TEMP_DB_PATH = Path("./data/contact_form_messages.json")

# - get all tags enums from schemas TagEnum (helps with populating form dropdown in frontend later)
# tbh idk if service layer is where i should put this but idt i can put it in models, and def not schemas...
def load_tags(): # "-> list[str]" would make sure it returns a string list
    return [tag.value for tag in TagEnum] #must return string list



# - get all messages list
# loads json data from file into Model objects
def load_messages() -> list[ContactFormMessageModel]: #-> list[ContactFormMessageModel]: makes sure it returns a list of ContactFormMessageModel's
    with open(TEMP_DB_PATH, "r") as f:
        data = json.load(f)
        return [ContactFormMessageModel(**message) for message in data["contact_form_messages_list"]] #ALT: or is it data.get("contact_form_messages_list", []) instead of data["messages"] ???
    
        # return [ContactFormMessageModel(**message).to_schema() for message in data["messages"]] 
        # ^ TODO: RESEARCH: could add .to_schema() but ig its better practice to just return the model from the service layer, and then convert the model to schema in the route layer...????

# - submit new message in contact form
# TEMP: APPENDS message to the json file. my fruits_service.py saves the entire list again, which is not very efficient, and def not what i would do when i connect with dynamoDB. 
def save_message(message: ContactFormMessageModel) -> None:
    with open(TEMP_DB_PATH, "r") as f:
        #load existing messages
        existing_data = json.load(f)
        messages = existing_data.get("contact_form_messages_list", [])
        
        #append new message to json file (since im not using an actual DB)
        messages.append(message.to_dict())
        
        # save updated list
        with open(TEMP_DB_PATH, "w") as f:
            json.dump({"contact_form_messages_list": messages}, f, indent=2)

# - delete messages
# @contact_form_router.delete("/messages")
# def delete_contact_form_messages():
#     return
def delete_message():
    return {"TODO"}