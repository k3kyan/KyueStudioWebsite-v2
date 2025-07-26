from pathlib import Path #temp for json db
import json #temp for json db
from models.contact_form_messages_models import ContactFormMessageModel #no need to import TagsEnum bc it doesnt exist in models, u dont have a separate json file or db for TagsEnum or anything
from schemas.contact_form_messages_schemas import TagEnum #only here for grabbing the tags from schemas.py

TEMP_DB_PATH = Path("./data/contact_form_messages.json")

# - get all tags enums from schemas TagEnum (helps with populating form dropdown in frontend later)
# tbh idk if service layer is where i should put this but idt i can put it in models, and def not schemas...
# @contact_form_router.get("/tags")
# def get_contact_form_tags_enums():
#     return [tag.value for tag in TagEnum]
def load_tags(): # "-> list[str]" would make sure it returns a string list
    return [tag.value for tag in TagEnum] #must return string list



# - get all messages list
# @contact_form_router.get("/messages-list")
# def get_contact_form_messages():
#     return
def load_messages():
    return {"TODO"}

# - submit new message in contact form
# @contact_form_router.post("/messages")
# def submit_contact_form_message(contact_form_message: ContactFormMessage):
#     return
def save_message(contact_form_message: ContactFormMessageModel):
    # with open(TEMP_DB_PATH, "w") as f:
    #     json.dump({"fruits": [contact_form_message.to_dict() for fruit in contact_form_message]}, f, indent=2)
    return {"TODO"}

# - delete messages
# @contact_form_router.delete("/messages")
# def delete_contact_form_messages():
#     return
def delete_message():
    return {"TODO"}