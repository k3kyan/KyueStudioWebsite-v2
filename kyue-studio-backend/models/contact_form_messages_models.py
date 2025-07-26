from schemas.contact_form_messages_schemas import ContactFormMessage, TagEnum
from typing import List

class ContactFormMessage:
    def __init__(
        self,
        firstName: str,
        lastName: str,
        email: str,
        subject: str,
        tags: List[str],
        message: str
    ):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.subject = subject
        self.tags = tags  # should be a list of string values like ["Bug Report", "Collaboration"]
        self.message = message
        
    # Actually jk im not gonna use this, doesnt seem as reliable or straightforward, even if more concise
    # # WARNING: This parameter more concise, BUT: its locking this constructor to only accept Pydantic schemas, so you have to use it like this now:
    # # VALID: ContactFormMessageModel(ContactFormMessage(...)) 
    # # INVALID: ContactFormMessageModel("Kelli", "Y", "k@k.com", ...)
    # def __init__(self, contact_form_message: ContactFormMessage):
    #     self.firstName = contact_form_message.firstName
    #     self.lastName = contact_form_message.lastName
    #     self.email = contact_form_message.email
    #     self.subject = contact_form_message.subject
    #     self.tags = contact_form_message.tags 
    #     self.message = contact_form_message.message
        
        
    # Method to create a Model from a Schema
    @classmethod
    def to_model(cls, schema: ContactFormMessage):
        return cls(
            firstName=schema.firstName,
            lastName=schema.lastName,
            email=schema.email,
            subject=schema.subject,
            tags=[tag.value for tag in schema.tags],  # convert Enum to list of str
            message=schema.message
        )
    
    
    # Method to create a Schema from a Model
    def to_schema(self):
        return ContactFormMessage(
            firstName=self.firstName,
            lastName=self.lastName,
            email=self.email,
            subject=self.subject,
            tags=[TagEnum(tag) for tag in self.tags],  # convert strings to Enum instances
            message=self.message
        )
    
    
    # Converts the model into a python dict for JSON/DB/jsonSerialization/etc
    # TODO: SWITCH: probably would change to format for DynamDB
    def to_dict(self):
        return {
            "firstName": self.firstName,
            "lastName": self.lastName,
            "email": self.email,
            "subject": self.subject,
            "tags": self.tags,  # just strings
            "message": self.message
        }
    