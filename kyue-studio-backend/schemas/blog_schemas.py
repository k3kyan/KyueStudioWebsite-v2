from pydantic import BaseModel, HttpUrl, Field
from typing import List, Optional
from datetime import date, datetime

# metadata (aka json files) is stored in DynamoDB
class BlogPostMetadataSchema(BaseModel):
    id: int
    title: str # = Field(..., min_length=1, max_length=100) #TODO: add this constraint later so it wont cause issues in the future
    tags: List[str]
    summary: str
    contentFileName: str # = Field(..., min_length=1) #TODO: add this constraint later so it wont cause issues in the future
    thumbnail_url: Optional[HttpUrl] = None
    date_created: datetime
    date_updated: Optional[datetime] = None
    
# content (aka markdown files) is stored in S3
class BlogPostContentSchema(BaseModel):
    id: int # TODO: IMPORTANT: MAKE SURE: THIS ID MATCHES THE METADATA'S ID !!!!
    contentFileName: str # = Field(..., min_length=1) #TODO: add this constraint later so it wont cause issues in the future
    
    
# full combined post, used in RESPONSE models !!!!
class BlogPostSchema(BaseModel):
    metadata: BlogPostMetadataSchema
    content: BlogPostContentSchema