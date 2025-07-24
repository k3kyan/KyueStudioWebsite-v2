# TODO: RESEARCH: ???? idk if this is correct
# schemas vs models: schemas are the database's model (json response?! idk), models are the pydantic models
# pydantic is used for data validation, schemas are used to create a table inside a database (??!??!?)
# from Ashutosh Pawar FastAPI udemy course, idk 

from pydantic import BaseModel

class Login(BaseModel):
    username: str
    password: str