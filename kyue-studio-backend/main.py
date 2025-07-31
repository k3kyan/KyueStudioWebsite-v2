import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from routes.fruit_routes import fruit_router #TEMP for testing
from fastapi.staticfiles import StaticFiles
# from routes.login_routes import login_router
from routes import fruit_routes, login_routes, authentication_routes, contact_form_messages_routes, blog_routes, test_routes #this way can import multiple routes in one line, less bloating
from auth import auth_handler
# loading env variables
from dotenv import load_dotenv, dotenv_values, find_dotenv
import os
from mangum import Mangum

# loads the .env.local file for whole project, only needs import os for other files to access .env.local variables
if os.getenv("ENV_MODE") == "local":
    load_dotenv(".env.local") 

# debugging, trying to call the environmental variables 
ALGORITHM = os.getenv("ALGORITHM")
print ("Admin username from main.py:", ALGORITHM)
BLOGPOSTSMETADATA_TABLE_NAME = os.getenv("BLOGPOSTSMETADATA_TABLE_NAME")
print ("BLOGPOSTSMETADATA_TABLE_NAME from main.py:", BLOGPOSTSMETADATA_TABLE_NAME)
ENV_MODE = os.getenv("ENV_MODE")
print ("ENV_MODE from main.py:", ENV_MODE)
KYUESTUDIOWEBSITES3BUCKETV2_BUCKET_NAME = os.getenv("KYUESTUDIOWEBSITES3BUCKETV2_BUCKET_NAME")
print ("KYUESTUDIOWEBSITES3BUCKETV2_BUCKET_NAME from main.py:", KYUESTUDIOWEBSITES3BUCKETV2_BUCKET_NAME)


# The FastAPI application/instance
app = FastAPI()

# Mount static uploads
# TODO: this doesnt load/work, idk why
# app.mount("/uploads", StaticFiles(directory="data/content/blog-posts"), name="uploads") #mounting all files from the blog-posts directory
app.mount("/thumbnails", StaticFiles(directory="data/content/blog-posts/blog_thumbnails"), name="thumbnails")
app.mount("/content", StaticFiles(directory="data/content/blog-posts/blog_content"), name="content")
app.mount("/metadata", StaticFiles(directory="data/content/blog-posts/blog_metadata"), name="metadata")

# Origins that are allowed, and given access to our API
# CORS setup
origins = [
    "http://localhost:3000",
    "http://localhost:8000",
    # "http://localhost:5173/", MAKE SURE TO NOT INCLUDE THAT LAST / !!!! that messed up the connectivity bc its not a valid origin. 
    "http://localhost:5173",
    "https://kyuestudio.com",
    "kyuestudio.com",
    "http://kyuestudio.com",
    # "https://kyuestudiowebsite.s3.us-east-2.amazonaws.com/index.html", TODO:?? is this a valid origin? prob. idk if its what i actually use tho for AWS later
    # "https://kyuestudio.com/" TODO: probably this origin...? probably, i'll get to that when i get to AWS migration
]

# FastAPI CORS middleware
# CORS = cross-origin resource sharing
# CORS prohibits/BLOCKS unauthorized websites, endpoints, or servers from accessing your API
# so only allows authorized trusted sources like our front end to interact with this backend app
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True, # allows cookies and sending JWT tokens etc
    allow_methods=["*"],
    allow_headers=["*"],
)


# registers APIRouters from other files here
# (in future, will include other routers like blog_router, cart_router, order_router, etc for diff APIs and db's and endpoints and paths)
app.include_router(fruit_router) #TEMP
app.include_router(login_routes.login_router)
app.include_router(authentication_routes.authentication_router) #Something went wrong when i added this before, but now i restarted app and its working now so idk, but if theres a problem in the future maybe check this ...?
app.include_router(contact_form_messages_routes.contact_form_router)
app.include_router(blog_routes.blog_router)
app.include_router(test_routes.test_router)

handler = Mangum(app)

# runs the uvicorn server
# runs the application for us
# To run from the terminal in Git Bash: python main.py
# i can probalby also run from VS code "run" button in the top right corner
if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)
    # is it 'main:app' or just app ?