from pydantic import BaseModel

# I think this would only be necessary for the methods i have commented out in auth/auth_handler.py for users ...? not sure
# POTENTIAL_ISSUE: Commented this out, hopefully it doesnt cause issues
# ?? TODO: FIX: do i even use this schema ??
# class Token(BaseModel):
#     access_token: str
#     token_type: str
    
# class TokenData(BaseModel):
#     username: str
    
# TODO: best place to put this?
# class Login(BaseModel):
#     username: str
#     password: str


# TODO: RESEARCH:
# the models might need less entities ??
# looking at Tech w Tim github, theres like 5 auth schemas but his models only have 1 for User, which lowkey the auth schemas could apply to. 
# Ig that makes sense since schemas are different RESPONSES from the API and models are the database models