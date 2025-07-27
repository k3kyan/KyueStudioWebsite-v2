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
    thumbnail_url: Optional[HttpUrl] = None
    contentFileName = str #TODO: RESEARCH: FIX: ??? is this right ??? ig it makes sense itd be a str bc its just the file name ???? (not including the .md part) // tho ig the filename is just the postid ..?? ldskfj
    date_created: datetime
    date_updated: Optional[datetime] = None
    

# # TODO: USELESS??
# # content (aka markdown files) is stored in S3
# # a post's metadata is only loaded when the post page is loaded since its so much bigger than the post's metadata
# # ok actually i think this is useless because I am never sending this object type in a response
# class BlogPostContentSchema(BaseModel):
#     id: uuid.UUID # TODO: IMPORTANT: MAKE SURE: THIS ID MATCHES THE METADATA'S ID !!!!
#     contentFileName: str # = Field(..., min_length=1) #TODO: add this constraint later so it wont cause issues in the future
    
    
# # TODO: USELESS??
# # full combined post, used in RESPONSE models !!!!
# class BlogPostSchema(BaseModel):
#     id: uuid.UUID # TODO: IMPORTANT: MAKE SURE: THIS ID MATCHES THE METADATA'S ID !!!! // tho u can access the id too from metadata.id or content.id
#     metadata: BlogPostMetadataSchema
#     content: BlogPostContentSchema
    
    
    
    
# ?????????????????????? ?? extra schemas specific to API response/return bodies ??!??! ?????????????????????? Not with db interactions/structures ???

# schema for what the API accepts when I submit a new post
# what the frontend sends when I submit a new post
# ?? wouldn't need a model since its only something submitted by api and not something loaded from db ????
# ig it is recommended to use two separate schemas for clarity...? makes sense
# Ok yeah im keeping this, its easier i think, makes sure our API gives us this exact data format
class BlogPostMetadataPOSTSchema(BaseModel):
    title: str # = Field(..., min_length=1, max_length=100) #TODO: add this constraint later so it wont cause issues in the future
    tags: List[str] #no restrictions, i will make type in my own tags at the time of making post
    summary: str
    thumbnail_url: Optional[HttpUrl] = None
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
    thumbnail_url: Optional[HttpUrl] = None
    # content ????
    