from fastapi import APIRouter, HTTPException
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

# Get list of tags, mostly for frontend to list out in a dropdown
@contact_form_router.get("/tags", response_model=List[TagEnum]) # REMINDER: FORGETFUL: DON'T FORGET RESPONSE BODY!!!! Otherwise it wont show up in SwaggerUI
def get_contact_form_tags_enums():
    return load_tags()

# PROTECTED ROUTE
# Get list of messages
@contact_form_router.get("/messages")
def get_contact_form_messages(token: str = Depends(oauth2_scheme)):
    return load_messages() #TODO: RESEARCH: should i be making this into a schema ...? ContactFormMessageModle.to_schema() ?? but doesnt the ** already do that (inside the method)?

# Submit a message to db
@contact_form_router.post("/message", response_model=ContactFormMessageSchema)
def submit_contact_form_message(message: ContactFormMessageSchema):
    model = ContactFormMessageModel.to_model(message) # Convert pydantic schema from API response body to json model for db
    save_message(model)
    return message


# PROTECTED ROUTE
# Delete individual method from db
@contact_form_router.delete("/message", response_model=dict) #response_model is just a dict (json response i think...?) #I don't need to import (from fastapi.responses import JSONResponse) right ??
def delete_contact_form_messages(email: str, subject: str, token: str = Depends(oauth2_scheme)):
    success = delete_message(email, subject)
    if not success:
        raise HTTPException(status_code=404, detail="Message not found. Nothing deleted.")
    return {"message": "Message deleted successfully."} # TODO: FIX: is this response ok?