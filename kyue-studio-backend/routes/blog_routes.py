from fastapi import APIRouter, UploadFile, HTTPException, status, Form, File
from schemas.blog_schemas import BlogPostMetadataSchema, BlogPostContentSchema, BlogPostSchema, BlogPostMetadataPOSTSchema
from typing import List
import uuid
from datetime import datetime
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


# PROTECTED ROUTE
# I submit post from admin frontend form
# backend (this endpoint/method) receives [???? what does this receive ????] what does frontend send when i post a new blog post ????
    # will i convert the response body here to separate content and metadata schemas ????
    # DO I CREATE A SEPARATE SCHEMA FOR THIS SPECIFIC RESPONSE ???
@blog_router.post("/post/create", response_model=dict) # WHAT IS THE response_model ?????? since i will have to add fields that arent in the BlogPostMetadataSchema schema like id ???
def create_blog_post(metadata: BlogPostMetadataPOSTSchema, content = File(...), token: str = Depends(oauth2_scheme)): # TODO: FIX: idk what im supposed to pass in too, this parameter is probably wrong sdlfkjs // removed "content: BlogPostContentSchema" parameter
    # should another parameter be: content_file: UploadFile = File(...) ?????
        # jk i dont need UploadFile bc i'm not uploading file ????? regarding the md content anyways, idk about the thumbnail later
    # title: str = Form(...), tags: List[str] = Form(...), summary: str = Form(...), thumbnail_url: Optional[str] = Form(...) ?????
        # i could probably just use these instead of making a new pydantic schema but idk, well see if it causes headache later
    # TODO: RESEARCH: PARAMETER content = File(...) will this take in / handle md content ????
    # NOTES: ??? So i guess the markdown will be sent as a STRING in a POST body json...
        # Researching more from google:
            # use multipart/form-data for md files because its suited to large content
        
    
    # TODO: upload image file
    # TODO: how to save content as markdown file ??
    
    post_id = uuid.uuid4() # generate id = uuid.UUID and save it to metadata
    post_datetime = datetime.now() #generate datetime
    
    
    
    # Save content to s3/markdown
    content =  content.file.read() # await ???
    contentFileName = f"{post_id}.md"
    with open(f"./data/content/blog-posts/{contentFileName}", "wb") as f: #TODO: AWS: would replace with wherever in s3 bucket idk #do i use wb or w ? // add "encoding="utf-8" ??
        f.write(content)
    # TODO: RESEARCH: in front end, to address md file upload.. use a <form> with enctype="multipart/form-data" and an <input type="file"> for the md content ????
    # TODO: RESEARCH: in front end, create a form specifically for handling md file content (and the metadata) etc ???
    # I think if i send as "multipart/form-data" in the front end, the backend will generate the file...????????
    # Send the markdown content as a STRING IN A JSON BODY IN THE REQUEST BODY, not the URL. // + POST/PUT requests allow larger payloads.
    # TODO: RESEARCH: tho... aws may charge more if the payload is bigger than 2MB or so.... // TODO: is there a way to cap the size of the payload? from frontend maybe? bc when its sent to the backend its already too late // maybe if its too large, you can separate the md content and send separate parts?
    
    # create metadata schema(?) instance using the POST metadata api schema
    metadata = BlogPostMetadataSchema(
        id=post_id, #from above
        title=metadata.title,
        tags=metadata.tags,
        summary=metadata.summary,
        thumbnail_url= None, #TODO: LATER: metadata.thumbnail_url, #TODO: LATER: how to handle uploading thumbnail image file ? // #how to do "or none" and use default thumbnail if no thumbnail is uploaded?
        contentFileName=contentFileName, # DOES include the .md extension (ok but the filename is just post_id + .md, do i need a new variable for it? ... it does add clarity so maybe i will lowkey. And i wont have to keep remembering to add .md at the end of everytime i call the method)
        date_created=post_datetime, #from above
        date_updated= None
    )
    
    # convert the pydantic schema api request body to json model for db
    # metadata is saved to DynamoDB/json
    save_post_metadata(metadata)
    
    
    
    
    # content is saved to s3/markdown
    return {"message": "Blog post created", "id": str(post_id)}



# get list of all blog posts
@blog_router.get("/posts")
def get_all_blog_posts(): #prob doesnt need parameters
    # prob just needs one method: load_posts()
    return {"TODO"}


# get one single blog post 
# GET /post/{id}
# backend loads metadata from db (uses ID)
# backend finds, matches, and loads content from s3 (uses ID)
# returns BlogPostSchema
@blog_router.get("/post/{id}") #?? correct ???? (TODO: RESEARCH: is this what a query parameter is...? idk the specifics sdlkfj )
def get_single_blog_post(id: uuid.UUID): #?? str or uuid.UUID ?? i think uuid because it ONLY becomes a string when saving from the db i think...? otherwise, its uuid for the entire react app i think...?
    return {"TODO"}



# PROTECTED ROUTE
# I update post from admin frontend form
# what is the response and return body ?? i do use both here probably
@blog_router.put("/post/{id}")
def update_blog_post(id: str, post: BlogPostSchema): #no idea if this is the correct parameters
    return {"TODO"}


# PROTECTED ROUTE
# I delete post (ONE OF THE ONLY THINGS THAT WILL PROVE IM LOGGED IN OR NOT FROM USER SIDE AND NOT JUST ADMIN PAGE, so nice for testing authentication)
@blog_router.delete("/post/{id}") #idk what the response model is
def delete_blog_post(id: str, token: str = Depends(oauth2_scheme)):
    # success = delete_message(id)
    # if not success:
    #     raise HTTPException(status_code=404, detail="Message not found. Nothing deleted.")
    return {"TODO"}