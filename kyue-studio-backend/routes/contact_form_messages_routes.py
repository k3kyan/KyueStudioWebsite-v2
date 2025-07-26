from fastapi import APIRouter
from schemas.contact_form_messages_schemas import ContactFormMessageSchema, TagEnum
from services.contact_form_messages_service import load_tags, load_messages, save_message, delete_message
from typing import List
from models.contact_form_messages_models import ContactFormMessageModel #IMPORTANT: PURELY HERE FOR CONVERSION METHODS !!! !!!!!!!

#For Authorization
from auth.auth_handler import oauth2_scheme
from fastapi import Depends

contact_form_router = APIRouter(
    prefix="/contact-form",
    tags=["contact-form"],
    # responses={404: {"description": "Not found"}}
)


# # TODO: Endpoints for:
# - get all tags enums (helps with populating form dropdown in frontend later)
# - get all messages list
# - submit new message in contact form
# - delete messages

@contact_form_router.get("/tags", response_model=List[TagEnum]) # DON'T FORGET RESPONSE BODY!!!! Otherwise it wont show up in SwaggerUI
def get_contact_form_tags_enums():
    return load_tags()

# TODO: probably protected
# Get list of messages
@contact_form_router.get("/messages")
def get_contact_form_messages(): # (TODO: add later in a single commit to highlight lol) token: str = Depends(oauth2_scheme)
    return load_messages() #TODO: RESEARCH: should i be making this into a schema ...? ContactFormMessageModle.to_schema() ?? but doesnt the ** already do that (inside the method)?


# From Fruits.py
# # @fruit_router.post("/fruits", response_model=FruitSchema)
# # def add_fruit(fruit: FruitSchema, token: str = Depends(oauth2_scheme)): # oh, all i needed to do to secure the endpoint was add the this "token: str = Depends(oauth2_scheme)" parameter in the endpoint method. p cool!!
# Submit a message to db
@contact_form_router.post("/message", response_model=ContactFormMessageSchema)
def submit_contact_form_message(message: ContactFormMessageSchema):
    model = ContactFormMessageModel.to_model(message) # Convert pydantic schema from API response body to json model for db
    save_message(model)
    return message



# Delete individual method from db
# protect route:    token: str = Depends(oauth2_scheme)
# @contact_form_router.delete("/message")
# def delete_contact_form_messages():
# delete_message()
#     return