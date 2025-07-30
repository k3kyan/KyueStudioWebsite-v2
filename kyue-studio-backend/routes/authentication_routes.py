from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm 
from auth import auth_handler
import os #to access .env.local environment variables
# AWS: no boto3 needed since it doesnt i/o with database



import boto3
from botocore.exceptions import ClientError


# code from AWS when i created secret
def get_secret():

    secret_name = "kyuestudio-creds"
    region_name = "us-east-2"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        # For a list of exceptions thrown, see
        # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
        raise e

    secret = get_secret_value_response['SecretString']
    return json.loads(secret)


authentication_router = APIRouter(
    # prefix="/auth",
    tags=["authentication"],
    # responses={404: {"description": "Not found"}}
)

# Creating the /token endpoint from auth_handler.py (oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token"))
# TODO: LATER: will need another depends parameter for getting user and verifying that password is correct (tho idk how that works with aws secrets manager ???)
@authentication_router.post("/token")
def authenticate_user(request: OAuth2PasswordRequestForm = Depends()): #db: Session = Depends(get_db))
    # load env variables (must load after fastapi app is connected!!) // also needs to be inside a method because it makes sure the .env.local was loaded up
    ENV_MODE = os.getenv("ENV_MODE", "aws").lower()
    if ENV_MODE == "aws":
        # Load admin credentials from AWS Secrets Manager
        secrets = get_secret()
        ADMIN_USERNAME = secrets.get("ADMIN_USERNAME")
        ADMIN_PASSWORD = secrets.get("ADMIN_PASSWORD")
    else:
        ADMIN_USERNAME = os.getenv("ADMIN_USERNAME")
        ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")
        # print ("Admin username from auth_routes.py:", ADMIN_USERNAME)
    
    # if invalid username
    if request.username != ADMIN_USERNAME:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")
    
    if request.password != ADMIN_PASSWORD: #did not decrypt/verify/hash/etc like in Catalin Stefan's tutorial
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")
    
    access_token = auth_handler.create_access_token(data={"sub": request.username}) # TODO: FIX: ??  not sure if "request.username" is correct // i think it should just be my username from AWS ?? the single one, not necessarily the one passed in, but ig if its reached that line then its correct/the same...?
    
    return {
        "access_token": access_token, 
        "token_type": "bearer"
        # "username": request.username
        # "user_id": ?? idk just whatever other data i'd wanna return , idk why i would tho but Catalin Stefan did it, i wont for now tho
        }