# i think only one file for models are neaded per feature (i.e. contactformmessages, fruits, blogposts, artwork, etc) 
# // (same with each module i think? so like each layer/module only has one file per feature..?)

# metadata and content have different models ???? / schemas ???? because they are stored in different file types AND different storage locations
# but i think they can be in the same file ???/ idk sldfjksljfs

# Note: when storing uuid.UUID to json/dynamodb, convert to string with str(uuid.UUID)
# To generate a new ID: uuid.uuid4()

from typing import List, Optional
from datetime import date, datetime
import uuid
from schemas.blog_schemas import BlogPostMetadataSchema, BlogPostContentSchema



# ------------------------------------------------- metadata model

# model for saving metadata to DynamoDB/json
class BlogPostMetadataModel:
    def __init__(
        self, 
        id: uuid.UUID,
        title: str,
        tags: List[str],
        summary: str,
        thumbnail_url: Optional[str],
        date_created: datetime,
        date_updated: Optional[datetime] = None
         ):
        self.id = id
        self.title = title
        self.tags = tags
        self.summary = summary
        self.thumbnail_url = thumbnail_url
        self.date_created = date_created
        self.date_updated = date_updated
        
    @classmethod
    def to_model(cls, schema: BlogPostMetadataSchema):
        return cls(
            id=uuid.UUID(str(schema.id)),  # TODO: RESEARCH: in case it's passed in as a string ?????
            title=schema.title,
            tags=schema.tags,
            summary=schema.summary,
            thumbnail_url=schema.thumbnail_url,
            date_created=schema.date_created,
            date_updated=schema.date_updated,
        )
        
    def to_schema(self):
        return BlogPostMetadataSchema(
            id=self.id,
            title=self.title,
            tags=self.tags,
            summary=self.summary,
            thumbnail_url=self.thumbnail_url,
            date_created=self.date_created,
            date_updated=self.date_updated,
        )
    
    # TODO: LATER: SWITCH: AWS: this is specific for json serialization, would adjust for dynamodb serialization later
    def to_dict(self):
        return {
            "id": str(self.id),  # convert UUID to string for JSON
            "title": self.title,
            "tags": self.tags,
            "summary": self.summary,
            "thumbnail_url": self.thumbnail_url,
            "date_created": self.date_created.isoformat(),
            "date_updated": self.date_updated.isoformat() if self.date_updated else None
        }
        
        
# # ------------------------------------------------- content model

# # TODO: do i even use this ??? 
# # model for saving content to S3
# class BlogPostContentModel:
#     def __init__(self, id: uuid.UUID, contentFileName: str):
#         self.id = id
#         self.contentFileName = contentFileName
        
#     def to_dict(self):
#         return {
#             "id": str(self.id),  # IMPORTANT: convert UUID to string for JSON !!!
#             "contentFileName": self.contentFileName
#         }
         
#     # TODO: IMPORTANT: !!!!!!!!!!
#     @classmethod
#     def from_dict(cls, data: dict):
#         return cls(
#             id=uuid.UUID(data["id"]),
#             content=data["content"]
#         )
        
#     # why no to_schema() or from_schema methods ???


# jk maybe this doesn't have a model since only the content and the metadata get saved to databases .......? yeah no need to save this to db bc its duplicate combined data
# class BlogPostModel:


# to_model()

# to_schema()

# to_dict() // responsible for serializing data into json-able format...? 