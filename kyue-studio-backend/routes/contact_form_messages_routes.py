from fastapi import APIRouter
from schemas.contact_form_messages_schemas import ContactFormMessage, TagEnum

contact_form_router = APIRouter(
    prefix="/contact-form",
    # tags=["contact-form-messages"],
    # responses={404: {"description": "Not found"}}
)


# # TODO: Endpoints for:
# - get all tags enums (helps with populating form dropdown in frontend later)
# - get all messages list
# - submit new message in contact form
# - delete messages

# @contact_form_router.get("/tags")
# def get_contact_form_tags_enums():
#     return [tag.value for tag in TagEnum]

# @contact_form_router.get("/messages-list")
# def get_contact_form_messages():
#     return

# @contact_form_router.post("/messages")
# def submit_contact_form_message(contact_form_message: ContactFormMessage):
#     return

# @contact_form_router.delete("/messages")
# def delete_contact_form_messages():
#     return