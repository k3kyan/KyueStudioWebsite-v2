from schemas.contact_form_messages_schemas import ContactFormMessageSchema, TagEnum
from typing import List

class ContactFormMessageModel:
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
        self.tags = tags  # should be a list of string values like ["Bug Report", "Collaboration"] #TODO: actually I only need 1 tag. The list of tags was for listing the tags for the dropdown. each message entity should just have ONE SINGLE tag!!!!! man... sislkdfjs
        self.message = message
        
    # Method to create a Model from a Schema
    # "from_schema()" is more standard naming convention for fastapi here, but i find it confusing for now, may change later
    @classmethod
    def to_model(cls, schema: ContactFormMessageSchema):
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
        return ContactFormMessageModel(
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
    