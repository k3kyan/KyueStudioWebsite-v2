from pydantic import BaseModel
from typing import List
from enum import Enum

# Enums list for the Tags dropdown. Edit to add/remove tags as needed. 
# TODO: Have your frontend send values like "Bug Report", "Feedback" (from a dropdown), so it matches your enum values.
# Cool functionality of FastAPI + Notes: 
# - FastAPI will validate that each tag sent is in the list of allowed enum values
# - Swagger UI will automatically render a multiple-choice picker
# - FastAPI will return 422 validation errors if a user submits an invalid tag
class TagEnum(str, Enum):
    collab = "Collaboration"
    job = "Job Opportunity"
    art_commission = "Art Commission"
    doll_commission = "Doll Commission"
    bug_report = "Bug Report"
    comments = "Comments on My Work"
    yapping = "Yapping & Other"

class ContactFormMessageSchema(BaseModel):
    firstName: str
    lastName: str
    email: str
    subject: str
    tags: List[TagEnum]
    message: str