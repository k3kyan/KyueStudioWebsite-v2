import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List


# fastapi can automatically validate data coming in
# and format data going out
# based on Pydantic models 
# TODO: PUT MODELS IN A SEPARATE FILE TO KEEP MAIN.PY CLEAN
class Fruit(BaseModel):
    name: str

class Fruits(BaseModel):
    fruits: List[Fruit]
    
    
    
    

# The FastAPI application/instance
app = FastAPI()


# Origins that are allowed, and given access to our API
origins = [
    "http://localhost:3000",
    "http://localhost:8000",
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



# TODO: replace this with a call to a json file (separate file..?). Prep for AWS DynamoDB calls. 
# TEMP_DATABASE
TEMP_DB = {"fruits": [
    {"name": "apple"},
    {"name": "banana"},
    {"name": "orange"}
]}


# TODO: move these functions/endpoints to a different file so main.py is cleaner. 
# need more modular abstraction separation

# returns data in the format model of class Fruits
@app.get("/fruits", response_model=Fruits)
def get_fruits():
    return Fruits(fruits=TEMP_DB["fruits"])


@app.post("/fruits", response_model=Fruit)
def add_fruit(fruit: Fruit):
    TEMP_DB["fruits"].append(fruit)
    return fruit



# runs the uvicorn server
# runs the application for us
# To run from the terminal in Git Bash: python main.py
# i can probalby also run from VS code "run" button in the top right corner
if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)
    # is it 'main:app' or just app ?