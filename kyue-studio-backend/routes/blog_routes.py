from fastapi import APIRouter, UploadFile, HTTPException, status, Form, File
from schemas.blog_schemas import BlogPostMetadataSchema, BlogPostMetadataPOSTSchema
from typing import List, Optional
import uuid
from pydantic import BaseModel, HttpUrl, Field
from datetime import date, datetime
from fastapi.responses import JSONResponse
import shutil
import json
from pathlib import Path
from fastapi.logger import logger
from services.blog_service import save_markdown_content, save_thumbnail, save_metadata, load_posts_metadata, load_single_post_metadata, delete_markdown_content, delete_thumbnail, delete_metadata #add more
# AWS: i THINK i dont need to change anything to boto3 because all the data i/o is taken care of in the service methods

#For Authorization
from auth.auth_handler import oauth2_scheme
from fastapi import Depends

blog_router = APIRouter(
    prefix="/blog",
    tags=["blog"],
    # responses={404: {"description": "Not found"}}
)

UPLOAD_DIR = "data/content/blog-posts"
Path(UPLOAD_DIR).mkdir(exist_ok=True)

# PROTECTED
# Create a new blog post from frontend admin form
@blog_router.post("/create-post")
async def create_post(
    metadata: str = Form(...),
    thumbnail: Optional[UploadFile] = File(None),
    content: UploadFile = File(...),
    token: str = Depends(oauth2_scheme)
):
    try:
        # Parse metadata
        print(f"Raw metadata: {metadata}")
        metadata_dict = json.loads(metadata) #NOT related to i/o, so no need to change for AWS. It's just parsing a json-formmatted string from a form field and converting to a python dictionary
        blog_meta = BlogPostMetadataPOSTSchema(**metadata_dict)
        
        # Generate metadata info not from frontend
        post_id = uuid.uuid4()
        created_at = datetime.now()

        # Save markdown content
        # print("\nContent.file:",  content.file) 
        content_path = save_markdown_content(post_id, content.file, UPLOAD_DIR)

        # Save thumbnail if present
        thumbnail_url = save_thumbnail(post_id, thumbnail, UPLOAD_DIR)
        
        # Use saved filenames
        content_filename = f"{post_id}_content.md"

        # Create full BlogPostMetadataSchema object
        full_metadata = BlogPostMetadataSchema(
            id=post_id,
            title=blog_meta.title,
            tags=blog_meta.tags,
            summary=blog_meta.summary,
            thumbnail_url=thumbnail_url,
            content_filename=content_filename,
            date_created=created_at,
            date_updated=None
        )
        
        # Save full metadata to file
        # don't need to save path since its not being added to metadata file.. since it is already the metadata file
        save_metadata(post_id, full_metadata, UPLOAD_DIR)
        
        
        return JSONResponse({
            "message": "Blog post received!",
            "metadata": blog_meta.model_dump(),
            "thumbnail_saved": bool(thumbnail),
            "content_saved_as": str(content_path.name),
        })

    except Exception as e:
        logger.error(f"Error in create_post: {e}")
        raise HTTPException(status_code=500, detail=str(e))

#     # TODO: RESEARCH: tho... aws may charge more if the payload is bigger than 2MB or so.... // TODO: is there a way to cap the size of the payload? from frontend maybe? bc when its sent to the backend its already too late 
#               // maybe if its too large, you can separate the md content and send separate parts?
#     # metadata is saved to DynamoDB/json
#     # content is saved to s3/markdown



# get list of all blog posts
@blog_router.get("/posts", response_model=List[BlogPostMetadataSchema])
async def get_all_blog_posts():
    all_posts = load_posts_metadata(UPLOAD_DIR)

    # Sort by newest first (based on date_created)
    all_posts.sort(key=lambda p: p.date_created, reverse=True)

    return all_posts


# # get one single blog post 
# # GET /post/{id}
@blog_router.get("/post/{post_id}", response_model=BlogPostMetadataSchema)
async def get_post_metadata(post_id: uuid.UUID):
    try:
        return load_single_post_metadata(post_id, UPLOAD_DIR)

    except Exception as e:
        logger.error(f"Error in get_post_metadata: {e}")
        raise HTTPException(status_code=500, detail="Failed to retrieve metadata")


# # PROTECTED ROUTE
# # I update post from admin frontend form
# # what is the response and return body ?? i do use both here probably
# @blog_router.put("/post/{id}")
# def update_blog_post(id: str, post: BlogPostSchema): #no idea if this is the correct parameters
#     return {"TODO"}


# # PROTECTED ROUTE
# # I delete post (ONE OF THE ONLY THINGS THAT WILL PROVE IM LOGGED IN OR NOT FROM USER SIDE AND NOT JUST ADMIN PAGE, so nice for testing authentication)
# @blog_router.delete("/post/{id}") #idk what the response model is // do i even need a response model actually....? its not taking in anything so ...? post id ?? idk
@blog_router.delete("/post/{post_id}")
async def delete_blog_post(post_id: uuid.UUID, token: str = Depends(oauth2_scheme)):
    try:
        # Delete content markdown file
        delete_markdown_content(post_id, UPLOAD_DIR)

        # Delete thumbnail if it's not the default
        delete_thumbnail(post_id, UPLOAD_DIR)

        # Delete the metadata file itself
        delete_metadata(post_id, UPLOAD_DIR)

        return {"message": f"Post {post_id} deleted."}

    except Exception as e:
        logger.error(f"Error deleting post {post_id}: {e}")
        raise HTTPException(status_code=500, detail="Failed to delete blog post")
