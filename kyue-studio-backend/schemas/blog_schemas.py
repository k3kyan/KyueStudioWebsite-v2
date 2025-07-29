from pydantic import BaseModel, HttpUrl, Field
from typing import List, Optional
from datetime import date, datetime
import uuid

# metadata (aka json files) is stored in DynamoDB
class BlogPostMetadataSchema(BaseModel):
    id: uuid.UUID #TODO: does schema have this as a UUID, but db saves as a string....? maybe that's handled by .to_dict() ??
    title: str # = Field(..., min_length=1, max_length=100) #TODO: add this constraint later so it wont cause issues in the future
    tags: List[str]
    summary: str
    thumbnail_url: str # Optional[HttpUrl] = None
    content_filename: str #TODO: RESEARCH: FIX: ??? is this right ??? ig it makes sense itd be a str bc its just the file name ???? (not including the .md part) // tho ig the filename is just the postid ..?? ldskfj
    date_created: datetime
    date_updated: Optional[datetime] = None
    
    
#  extra schemas specific to API response/return bodies // Not with db interactions/structures ???

# schema for what the API accepts when I submit a new post
# what the frontend sends when I submit a new post
# Ok yeah im keeping this, its easier i think, makes sure our API gives us this exact data format
class BlogPostMetadataPOSTSchema(BaseModel):
    title: str # = Field(..., min_length=1, max_length=100) #TODO: add this constraint later so it wont cause issues in the future
    tags: List[str] #no restrictions, i will make type in my own tags at the time of making post
    summary: str
    thumbnail_url: str #Optional[HttpUrl] = None
    content_filename: str #TODO: IMPORTANT !!!!!!!!!!!!!!!!! NOT PUT INTO THE MODELS YET!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # Actually do i even need thumbnail_url and content_filename ..? it works fine without it... hm 
    # would assign contentFileName not in the api, but inside the create_post() endpoint method i think
    
    
# TODO: FIX: RESEARCH:
# schema for what the API accepts when I update a post ??? needed?? necessary??? idk maybe not ????
# has editable fields only like title, tags, NOT id or datecreated, etc ????
# class BlogPostUpdateSchema(BlogPostMetadataSchema):
# only editable fields
class BlogPostMetadataPUTSchema(BaseModel):
    # id ?? how else will ti find the content ??
    title: str # = Field(..., min_length=1, max_length=100) #TODO: add this constraint later so it wont cause issues in the future
    tags: List[str] #no restrictions, i will make type in my own tags at the time of making post
    summary: str
    thumbnail_url: str #Optional[HttpUrl] = None
    # content ????
    