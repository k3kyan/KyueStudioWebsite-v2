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
# from services.blog_service import 
# will need more imports later, just drafting rn

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

# Create a new blog post from frontend admin form
# TODO: separate into service methods for 1) save markdown content 2) save thumbnail 3) create and save full combined metadata
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
        metadata_dict = json.loads(metadata)
        blog_meta = BlogPostMetadataPOSTSchema(**metadata_dict)
        
        # Generate metadata info not from frontend
        post_id = uuid.uuid4()
        created_at = datetime.now()

        # Save markdown content
        content_path = Path(UPLOAD_DIR) / "blog_content"/ f"{post_id}_content.md"
        with content_path.open("wb") as f:
            shutil.copyfileobj(content.file, f)
        # content_filename = content_path.name # store just the filename for metadata

        # Save thumbnail if present
        # if thumbnail:
        #     thumb_path = Path(UPLOAD_DIR) / "blog_thumbnails"/ thumbnail.filename
        #     with thumb_path.open("wb") as f:
        #         shutil.copyfileobj(thumbnail.file, f)
        # Save thumbnail if present
        if thumbnail:
            thumb_path = Path(UPLOAD_DIR) / "blog_thumbnails" / f"{post_id}_{thumbnail.filename}"
            thumb_path.parent.mkdir(parents=True, exist_ok=True)  # ensure folder exists
            with thumb_path.open("wb") as f:
                shutil.copyfileobj(thumbnail.file, f)
            # thumbnail_url = f"/{thumb_path.as_posix()}"
            thumbnail_url = f"{post_id}_{thumbnail.filename}" #TODO: changed to only be filename, not path
        else:
            default_thumb = Path("data/content/blog-posts/blog_thumbnails/default-thumbnail.jpg")
            thumbnail_url = f"/{default_thumb.as_posix()}"
            
                
        
        # Use saved filenames
        content_path = Path(UPLOAD_DIR) / content.filename
        content_filename = content_path.name

        # REMOVE: duplicate code of above
        # if thumbnail:
        #     thumb_path = Path(UPLOAD_DIR) / thumbnail.filename
        #     thumbnail_url = f"/{UPLOAD_DIR}/{thumbnail.filename}"
        # else:
        #     default_thumb = Path("data/content/blog-posts/blog_thumbnails/default-thumbnail.jpg")
        #     thumbnail_url = f"/{default_thumb.as_posix()}"

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
        metadata_path = Path(UPLOAD_DIR) / f"blog_metadata/{post_id}_metadata.json"
        with metadata_path.open("w", encoding="utf-8") as f:
            json.dump(full_metadata.model_dump(), f, indent=2, default=str)

        return JSONResponse({
            "message": "Blog post received!",
            "metadata": blog_meta.model_dump(),
            "thumbnail_saved": bool(thumbnail),
            "content_saved_as": str(content_path.name),
        })

    except Exception as e:
        logger.error(f"Error in create_post: {e}")
        raise HTTPException(status_code=500, detail=str(e))








# # PROTECTED ROUTE
# # I submit post from admin frontend form
# # backend (this endpoint/method) receives [???? what does this receive ????] what does frontend send when i post a new blog post ????
#     # will i convert the response body here to separate content and metadata schemas ????
#     # DO I CREATE A SEPARATE SCHEMA FOR THIS SPECIFIC RESPONSE ???
# @blog_router.post("/post/create", response_model=dict) # WHAT IS THE response_model ?????? since i will have to add fields that arent in the BlogPostMetadataSchema schema like id ???
# def create_blog_post(metadata: BlogPostMetadataPOSTSchema, content = File(...), token: str = Depends(oauth2_scheme)): # TODO: FIX: idk what im supposed to pass in too, this parameter is probably wrong sdlfkjs // removed "content: BlogPostContentSchema" parameter
#     # should another parameter be: content_file: UploadFile = File(...) ?????
#         # jk i dont need UploadFile bc i'm not uploading file ????? regarding the md content anyways, idk about the thumbnail later
#     # title: str = Form(...), tags: List[str] = Form(...), summary: str = Form(...), thumbnail_url: Optional[str] = Form(...) ?????
#         # i could probably just use these instead of making a new pydantic schema but idk, well see if it causes headache later
#     # TODO: RESEARCH: PARAMETER content = File(...) will this take in / handle md content ????
#     # NOTES: ??? So i guess the markdown will be sent as a STRING in a POST body json...
#         # Researching more from google:
#             # use multipart/form-data for md files because its suited to large content
        
    
#     # TODO: upload image file
#     # TODO: how to save content as markdown file ??
    
#     post_id = uuid.uuid4() # generate id = uuid.UUID and save it to metadata
#     post_datetime = datetime.now() #generate datetime
    
    
    
#     # Save content to s3/markdown
#     content =  content.file.read() # await ???
#     contentFileName = f"{post_id}.md"
#     with open(f"./data/content/blog-posts/{contentFileName}", "wb") as f: #TODO: AWS: would replace with wherever in s3 bucket idk #do i use wb or w ? // add "encoding="utf-8" ??
#         f.write(content)
#     # TODO: RESEARCH: in front end, to address md file upload.. use a <form> with enctype="multipart/form-data" and an <input type="file"> for the md content ????
#     # TODO: RESEARCH: in front end, create a form specifically for handling md file content (and the metadata) etc ???
#     # I think if i send as "multipart/form-data" in the front end, the backend will generate the file...????????
#     # Send the markdown content as a STRING IN A JSON BODY IN THE REQUEST BODY, not the URL. // + POST/PUT requests allow larger payloads.
#     # TODO: RESEARCH: tho... aws may charge more if the payload is bigger than 2MB or so.... // TODO: is there a way to cap the size of the payload? from frontend maybe? bc when its sent to the backend its already too late // maybe if its too large, you can separate the md content and send separate parts?
    
#     # create metadata schema(?) instance using the POST metadata api schema
#     metadata = BlogPostMetadataSchema(
#         id=post_id, #from above
#         title=metadata.title,
#         tags=metadata.tags,
#         summary=metadata.summary,
#         thumbnail_url= None, #TODO: LATER: metadata.thumbnail_url, #TODO: LATER: how to handle uploading thumbnail image file ? // #how to do "or none" and use default thumbnail if no thumbnail is uploaded?
#         contentFileName=contentFileName, # DOES include the .md extension (ok but the filename is just post_id + .md, do i need a new variable for it? ... it does add clarity so maybe i will lowkey. And i wont have to keep remembering to add .md at the end of everytime i call the method)
#         date_created=post_datetime, #from above
#         date_updated= None
#     )
    
#     # convert the pydantic schema api request body to json model for db
#     # metadata is saved to DynamoDB/json
#     save_post_metadata(metadata)
    
    
    
    
#     # content is saved to s3/markdown
#     return {"message": "Blog post created", "id": str(post_id)}




# # ----------------------------------- maybe need to do a separate call for each function? 1) sending metadata, 2) sending photo upload, 3) sending content md 
# TODO: i should def do separate service calls 
# # send thumbnail
# @blog_router.post("/api/upload-thumbnail")
# async def upload_thumbnail(file: UploadFile = File(...)):
#     file_path = f"thumbnails/{uuid4()}.png"
#     with open(file_path, "wb") as f:
#         f.write(await file.read())
#     return {"filePath": file_path}


# # send markdown content
# @blog_router.post("/api/upload-content")
# async def upload_md(file: UploadFile = File(...)):
#     file_path = f"blog_content/{uuid4()}.md"
#     with open(file_path, "wb") as f:
#         f.write(await file.read())
#     return {"filePath": file_path}


# # send metadata
# @blog_router.post("/api/create-post")
# async def create_post(post: BlogPostMetadataPOSTSchema):
#     # Store in JSON for now or DynamoDB later
#     metadata_path = f"metadata/{uuid4()}.json"
#     with open(metadata_path, "w") as f:
#         json.dump(post.dict(), f)
#     return {"status": "success"}






















































# # get list of all blog posts
# @blog_router.get("/posts")
# def get_all_blog_posts(): #prob doesnt need parameters
#     # prob just needs one method: load_posts()
#     return {"TODO"}

@blog_router.get("/posts", response_model=List[BlogPostMetadataSchema])
async def get_all_blog_posts():
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

    # Sort by newest first (based on date_created)
    all_posts.sort(key=lambda p: p.date_created, reverse=True)

    return all_posts


# # get one single blog post 
# # GET /post/{id}
# # backend loads metadata from db (uses ID)
# # backend finds, matches, and loads content from s3 (uses ID)
# # returns BlogPostSchema
# @blog_router.get("/post/{id}") #?? correct ???? (TODO: RESEARCH: is this what a query parameter is...? idk the specifics sdlkfj )
# def get_single_blog_post(id: uuid.UUID): #?? str or uuid.UUID ?? i think uuid because it ONLY becomes a string when saving from the db i think...? otherwise, its uuid for the entire react app i think...?
#     return {"TODO"}


@blog_router.get("/post/{post_id}", response_model=BlogPostMetadataSchema)
async def get_post_metadata(post_id: uuid.UUID):
    try:
        metadata_path = Path(UPLOAD_DIR) / "blog_metadata" / f"{post_id}_metadata.json"

        if not metadata_path.exists():
            raise HTTPException(status_code=404, detail="Post metadata not found")

        with metadata_path.open("r", encoding="utf-8") as f:
            metadata_dict = json.load(f)

        return BlogPostMetadataSchema(**metadata_dict)

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
# @blog_router.delete("/post/{id}") #idk what the response model is
# def delete_blog_post(id: str, token: str = Depends(oauth2_scheme)):
#     # success = delete_message(id)
#     # if not success:
#     #     raise HTTPException(status_code=404, detail="Message not found. Nothing deleted.")
#     return {"TODO"}


@blog_router.delete("/post/{post_id}")
async def delete_blog_post(post_id: uuid.UUID, token: str = Depends(oauth2_scheme)):
    try:
        metadata_path = Path(UPLOAD_DIR) / "blog_metadata" / f"{post_id}_metadata.json"

        if not metadata_path.exists():
            raise HTTPException(status_code=404, detail="Metadata not found")

        # Load metadata
        with metadata_path.open("r", encoding="utf-8") as f:
            metadata = json.load(f)

        # Delete content markdown file
        content_path = Path(UPLOAD_DIR) / "blog_content" / metadata["content_filename"]
        if content_path.exists():
            content_path.unlink()

        # Delete thumbnail if it's not the default
        thumbnail_url = metadata.get("thumbnail_url", "")
        if (
            thumbnail_url
            and "default-thumbnail" not in thumbnail_url
            and "blog_thumbnails" in thumbnail_url
        ):
            thumbnail_filename = Path(thumbnail_url).name
            thumbnail_path = Path(UPLOAD_DIR) / "blog_thumbnails" / thumbnail_filename
            if thumbnail_path.exists():
                thumbnail_path.unlink()

        # Delete the metadata file itself
        metadata_path.unlink()

        return {"message": f"Post {post_id} deleted."}

    except Exception as e:
        logger.error(f"Error deleting post {post_id}: {e}")
        raise HTTPException(status_code=500, detail="Failed to delete blog post")
