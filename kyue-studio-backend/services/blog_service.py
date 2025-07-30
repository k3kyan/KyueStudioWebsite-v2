from pathlib import Path #temp for json db
import json #temp for json db
import shutil
import uuid
from fastapi import UploadFile, HTTPException, status, Form, File
from typing import Optional, List
from fastapi.logger import logger
from schemas.blog_schemas import BlogPostMetadataSchema, BlogPostMetadataPOSTSchema
# from models.blog_models import BlogPostMetadataModel #no need to import TagsEnum bc it doesnt exist in models, u dont have a separate json file or db for TagsEnum or anything
import os
import boto3


# is this where the schemas get sorted into different models / schemas ????



# load_content_from_s3() 

# Examples that work
# http://localhost:8000/thumbnails/48f4d4fd-7aef-4801-87ab-b811837582ed_pixelcitybg.png
# http://localhost:8000/content/0380b2d8-187c-4403-a0fa-7a0141d5d0eb_content.md
# http://localhost:8000/blog/post/48f4d4fd-7aef-4801-87ab-b811837582ed
# http://localhost:8000/thumbnails/aba2fcb9-9628-4f4a-a537-ea08fdac0990_steam-logo.jpg
# http://localhost:8000/thumbnails/48f4d4fd-7aef-4801-87ab-b811837582ed_pixelcitybg.png

# for @blog_router.post("/create-post")
# async def create_post(
# 1) save markdown content 
def save_markdown_content(post_id: uuid.UUID, content_file, UPLOAD_DIR: str):
    ENV_MODE = os.getenv("ENV_MODE", "aws").lower()
    if ENV_MODE == "aws":
        content_filename = f"{post_id}_content.md"
        s3 = boto3.client("s3")
        bucket_name = os.getenv("KYUESTUDIOWEBSITES3BUCKETV2_BUCKET_NAME")

        # Read file content into memory (assuming content_file is a file-like object)
        try:
            s3.put_object(
                Bucket=bucket_name,
                Key=f"posts/{content_filename}",  # Customize prefix if needed
                Body=content_file,
                ContentType="text/markdown"
            )
            return f"posts/{content_filename}"  # return S3 key
        except Exception as e:
            print(f"Error uploading markdown to S3: {e}")
            raise
    else:
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
        ENV_MODE = os.getenv("ENV_MODE", "aws").lower()
        if ENV_MODE == "aws":
            thumbnail_filename = f"{post_id}_{thumbnail.filename}" if thumbnail else "default-thumbnail.jpg"

            s3 = boto3.client("s3")
            bucket = os.getenv("KYUESTUDIOWEBSITES3BUCKETV2_BUCKET_NAME")

            if thumbnail:
                try:
                    s3.put_object(
                        Bucket=bucket,
                        Key=f"thumbnails/{thumbnail_filename}",
                        Body=thumbnail.file,
                        ContentType=thumbnail.content_type
                    )
                    return f"thumbnails/{thumbnail_filename}"
                except Exception as e:
                    print(f"Error uploading thumbnail to S3: {e}")
                    raise
            else:
                # Optional: You could point to a known public default in S3
                return "thumbnails/default-thumbnail.jpg"
            
        else:
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
    ENV_MODE = os.getenv("ENV_MODE", "aws").lower()
    if ENV_MODE == "aws":
        metadata_dict = full_metadata.model_dump()
        metadata_dict["id"] = str(post_id)  # Ensure ID is string
        
        try:
            # Convert datetime fields to strings
            for key in ["date_created", "date_updated"]:
                if key in metadata_dict and metadata_dict[key] is not None:
                    metadata_dict[key] = str(metadata_dict[key])

            dynamodb = boto3.resource("dynamodb")
            table = dynamodb.Table(os.getenv("BLOGPOSTSMETADATA_TABLE_NAME"))
            table.put_item(Item=metadata_dict)

        except Exception as e:
            print(f"Error saving metadata to DynamoDB: {e}")
            raise
    else:
        metadata_path = Path(UPLOAD_DIR) / f"blog_metadata/{post_id}_metadata.json"
        with metadata_path.open("w", encoding="utf-8") as f:
            json.dump(full_metadata.model_dump(), f, indent=2, default=str)


# @blog_router.get("/posts", response_model=List[BlogPostMetadataSchema])
# async def get_all_blog_posts():
def load_posts_metadata(UPLOAD_DIR: str) -> List[BlogPostMetadataSchema]:
    ENV_MODE = os.getenv("ENV_MODE", "aws").lower()
    if ENV_MODE == "aws":
        try:
            dynamodb = boto3.resource("dynamodb")
            table = dynamodb.Table(os.getenv("BLOGPOSTSMETADATA_TABLE_NAME"))
            response = table.scan()
            items = response.get("Items", [])

            all_posts = []
            for item in items:
                try:
                    post = BlogPostMetadataSchema(**item)
                    all_posts.append(post)
                except Exception as e:
                    logger.warning(f"Skipped DynamoDB item due to error: {e}")
            return all_posts

        except Exception as e:
            logger.error(f"Error scanning DynamoDB: {e}")
            return []

    else:
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
    ENV_MODE = os.getenv("ENV_MODE", "aws").lower()
    if ENV_MODE == "aws":
        try:
            dynamodb = boto3.resource("dynamodb")
            table = dynamodb.Table(os.getenv("BLOGPOSTSMETADATA_TABLE_NAME"))
            response = table.get_item(Key={"id": str(post_id)})
            item = response.get("Item")

            if not item:
                raise HTTPException(status_code=404, detail="Post metadata not found")

            return BlogPostMetadataSchema(**item)

        except Exception as e:
            print(f"Error loading metadata from DynamoDB: {e}")
            raise HTTPException(status_code=500, detail="Failed to load metadata from DynamoDB")

    else:
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
    ENV_MODE = os.getenv("ENV_MODE", "aws").lower()
    if ENV_MODE == "aws":
        metadata = load_metadata(post_id, UPLOAD_DIR)
        content_filename = metadata.content_filename
        
        if not content_filename:
            return  # Nothing to delete
        
        try:
            s3 = boto3.client("s3")
            bucket = os.getenv("KYUESTUDIOWEBSITES3BUCKETV2_BUCKET_NAME")
            s3.delete_object(Bucket=bucket, Key=f"posts/{content_filename}")
        except Exception as e:
            print(f"Error deleting markdown content from S3: {e}")
            raise
    else:
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
    ENV_MODE = os.getenv("ENV_MODE", "aws").lower()
    if ENV_MODE == "aws":
        metadata = load_metadata(post_id, UPLOAD_DIR)
        thumbnail_url = getattr(metadata, "thumbnail_url", "")
        if not thumbnail_url or "default-thumbnail" in thumbnail_url:
            return  # Nothing to delete

        thumbnail_filename = Path(thumbnail_url).name
        try:
            s3 = boto3.client("s3")
            bucket = os.getenv("KYUESTUDIOWEBSITES3BUCKETV2_BUCKET_NAME")
            s3.delete_object(Bucket=bucket, Key=f"thumbnails/{thumbnail_filename}")
        except Exception as e:
            print(f"Error deleting thumbnail from S3: {e}")
            raise
    else:
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
    ENV_MODE = os.getenv("ENV_MODE", "aws").lower()
    if ENV_MODE == "aws":
        try:
            dynamodb = boto3.resource("dynamodb")
            table = dynamodb.Table(os.getenv("BLOGPOSTSMETADATA_TABLE_NAME"))
            table.delete_item(Key={"id": str(post_id)})
        except Exception as e:
            print(f"Error deleting metadata from DynamoDB: {e}")
            raise
    else:
        # metadata = load_metadata(post_id, UPLOAD_DIR)
        metadata_path = Path(UPLOAD_DIR) / "blog_metadata" / f"{post_id}_metadata.json"
        metadata_path.unlink()
        # return "success" maybe?
