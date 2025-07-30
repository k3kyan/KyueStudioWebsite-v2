# used for testing connection to AWS API
from fastapi import APIRouter
from fastapi.responses import JSONResponse
import os
import boto3
import json

test_router = APIRouter(
    prefix="/test",
    tags=["test"],
    responses={404: {"description": "Not found"}},
)

# Helper clients
dynamodb = boto3.client("dynamodb")
# secretsmanager = boto3.client("secretsmanager")

# Example: Use env vars for names
DYNAMODB_TABLE = os.getenv("CONTACT_MESSAGES_TABLE")
S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME")
# SECRET_NAME_ADMIN_USERNAME = os.getenv("ADMIN_USERNAME")
ENV_MODE = os.getenv("ENV_MODE")  # optional env var

# returns plain json response
@test_router.get("/")
async def get_plain_json():
    return {"message": "Hello World"}

# returns my dynamodb table name
@test_router.get("/dynamodb-name")
def get_dynamodb_table_name():
    return {"table_name": DYNAMODB_TABLE}

# returns the dynamodb table info (using boto3)
@test_router.get("/dynamodb-info")
def get_dynamodb_table_info():
    try:
        response = dynamodb.describe_table(TableName=DYNAMODB_TABLE)
        return response["Table"]
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
    
# returns my s3 bucket name
@test_router.get("/s3-bucket")
def get_s3_bucket():
    return {"bucket_name": S3_BUCKET_NAME}

# returns a lambda environment variable ENV_MODE
@test_router.get("/env-stage")
def get_env_stage():
    return {"env_mode": ENV_MODE}

# # returns a secrets manager variable?
# # this one probably wont work since secrets manager gave me specific code
# @router.get("/test/secret")
# def get_secret_value():
#     try:
#         secret = secretsmanager.get_secret_value(SecretId=SECRET_NAME)
#         return {"secret": json.loads(secret["SecretString"])}
#     except Exception as e:
#         return JSONResponse(status_code=500, content={"error": str(e)})