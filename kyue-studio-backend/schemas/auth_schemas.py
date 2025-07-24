from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    username: str
    
# TODO: best place to put this?
# class Login(BaseModel):
#     username: str
#     password: str