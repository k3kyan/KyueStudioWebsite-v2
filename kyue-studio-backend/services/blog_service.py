from pathlib import Path #temp for json db
import json #temp for json db
import shutil
import uuid
from fastapi import UploadFile, HTTPException, status, Form, File
from typing import Optional, List
from fastapi.logger import logger
from schemas.blog_schemas import BlogPostMetadataSchema, BlogPostMetadataPOSTSchema
# from models.blog_models import BlogPostMetadataModel #no need to import TagsEnum bc it doesnt exist in models, u dont have a separate json file or db for TagsEnum or anything



# is this where the schemas get sorted into different models / schemas ????



# load_content_from_s3() 



# for @blog_router.post("/create-post")
# async def create_post(
# 1) save markdown content 
def save_markdown_content(post_id: uuid.UUID, content_file, UPLOAD_DIR: str):
    content_path = Path(UPLOAD_DIR) / "blog_content"/ f"{post_id}_content.md"
    with content_path.open("wb") as f:
        shutil.copyfileobj(content_file, f)
    return content_path

# 2) save thumbnail 
def save_thumbnail(
    post_id: uuid.UUID,
    thumbnail: Optional[UploadFile],
    UPLOAD_DIR: str,
    default_thumb: str = "data/content/blog-posts/blog_thumbnails/default-thumbnail.jpg"
    ):
        if thumbnail:
            thumb_path = Path(UPLOAD_DIR) / "blog_thumbnails" / f"{post_id}_{thumbnail.filename}"
            with thumb_path.open("wb") as f:
                shutil.copyfileobj(thumbnail.file, f)
            # thumbnail_url = f"/{thumb_path.as_posix()}"
            thumbnail_url = f"{post_id}_{thumbnail.filename}" #TODO: changed to only be filename, not path
        else:
            default_thumb = Path("data/content/blog-posts/blog_thumbnails/default-thumbnail.jpg")
            thumbnail_url = f"/{default_thumb.as_posix()}"
            
        return thumbnail_url

# 3) create and save full combined metadata
def save_metadata(post_id: uuid.UUID, full_metadata: BlogPostMetadataSchema, UPLOAD_DIR: str):
    metadata_path = Path(UPLOAD_DIR) / f"blog_metadata/{post_id}_metadata.json"
    with metadata_path.open("w", encoding="utf-8") as f:
        json.dump(full_metadata.model_dump(), f, indent=2, default=str)


# @blog_router.get("/posts", response_model=List[BlogPostMetadataSchema])
# async def get_all_blog_posts():
def load_posts_metadata(UPLOAD_DIR: str) -> List[BlogPostMetadataSchema]:
    metadata_dir = Path(UPLOAD_DIR) / "blog_metadata"
    all_posts = []

    for file in metadata_dir.glob("*.json"):
        try:
            with file.open("r", encoding="utf-8") as f:
                data = json.load(f)
                post = BlogPostMetadataSchema(**data)
                all_posts.append(post)
        except Exception as e:
            logger.warning(f"Skipped file {file.name} due to error: {e}")
            
    return all_posts
# 1. since this will be different in dynamodb, just lowkey put all of it into one function that returns all the posts


# @blog_router.get("/post/{post_id}", response_model=BlogPostMetadataSchema)
# async def get_post_metadata(post_id: uuid.UUID):
# 1. method to get the metadata (keep inside try catch block)
def load_single_post_metadata(post_id: uuid.UUID, UPLOAD_DIR: str) -> BlogPostMetadataSchema:
        metadata_path = Path(UPLOAD_DIR) / "blog_metadata" / f"{post_id}_metadata.json"

        if not metadata_path.exists():
            raise HTTPException(status_code=404, detail="Post metadata not found")

        with metadata_path.open("r", encoding="utf-8") as f:
            metadata_dict = json.load(f)

        return BlogPostMetadataSchema(**metadata_dict)


# @blog_router.delete("/post/{post_id}")
# async def delete_blog_post(post_id: uuid.UUID, token: str = Depends(oauth2_scheme)):
# this load_metadata method is redundant but it helps me think so. I only use it internally here. 
def load_metadata(post_id: uuid.UUID, UPLOAD_DIR: str) -> BlogPostMetadataSchema:
    return load_single_post_metadata(post_id, UPLOAD_DIR)

# 1. method to delete content markdown file (parameter is post_id)
def delete_markdown_content(post_id: uuid.UUID, UPLOAD_DIR: str):
    # load specific post's metadata so we can find what to delete
    metadata = load_metadata(post_id, UPLOAD_DIR)
    
    # delete content markdown file
    # content_path = Path(UPLOAD_DIR) / "blog_content" / metadata["content_filename"]
    content_path = Path(UPLOAD_DIR) / "blog_content" / metadata.content_filename
    if content_path.exists():
        content_path.unlink()
    # return "success" maybe?
            
# 2. method to delete thumbnail if it's not the default (parameter is post_id)
def delete_thumbnail(post_id: uuid.UUID, UPLOAD_DIR: str):
    # load specific post's metadata so we can find what to delete
    metadata = load_metadata(post_id, UPLOAD_DIR)
    
    # delete thumbnail
    # thumbnail_url = metadata.get("thumbnail_url", "")
    thumbnail_url = getattr(metadata, "thumbnail_url", "")
    if (
        thumbnail_url
        and "default-thumbnail" not in thumbnail_url
        and "blog_thumbnails" in thumbnail_url
    ):
        thumbnail_filename = Path(thumbnail_url).name
        thumbnail_path = Path(UPLOAD_DIR) / "blog_thumbnails" / thumbnail_filename
        if thumbnail_path.exists():
            thumbnail_path.unlink()
    # return "success" maybe?

# 3. method to delete the metadata file  (parameter is post_id)
def delete_metadata(post_id: uuid.UUID, UPLOAD_DIR: str):
    # metadata = load_metadata(post_id, UPLOAD_DIR)
    metadata_path = Path(UPLOAD_DIR) / "blog_metadata" / f"{post_id}_metadata.json"
    metadata_path.unlink()
    # return "success" maybe?
