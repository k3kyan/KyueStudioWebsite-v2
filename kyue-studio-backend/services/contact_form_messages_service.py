from pathlib import Path #temp for json db
import json #temp for json db
from models.contact_form_messages_models import ContactFormMessageModel #no need to import TagsEnum bc it doesnt exist in models, u dont have a separate json file or db for TagsEnum or anything
from schemas.contact_form_messages_schemas import TagEnum #only here for grabbing the tags from schemas.py
import os
import boto3

TEMP_DB_PATH = Path("./data/contact_form_messages.json")

# - get all tags enums from schemas TagEnum (helps with populating form dropdown in frontend later)
# tbh idk if service layer is where i should put this but idt i can put it in models, and def not schemas...
def load_tags(): # "-> list[str]" would make sure it returns a string list
    return [tag.value for tag in TagEnum] #must return string list



# - get all messages list
# loads json data from file into Model objects
def load_messages() -> list[ContactFormMessageModel]: #-> list[ContactFormMessageModel]: makes sure it returns a list of ContactFormMessageModel's
    ENV_MODE = os.getenv("ENV_MODE", "aws").lower()
    if ENV_MODE == "aws":
        # Load from DynamoDB
        dynamodb = boto3.resource("dynamodb")
        table = dynamodb.Table(os.getenv("CONTACTFORMMESSAGES_TABLE_NAME"))
        
        try:
            response = table.scan()
            items = response.get("Items", [])
            return [ContactFormMessageModel(**item) for item in items]
        except Exception as e:
            print(f"Error loading messages from DynamoDB: {e}")
            return []
    else:
        # load with local json file
        with open(TEMP_DB_PATH, "r") as f:
            data = json.load(f)
            return [ContactFormMessageModel(**message) for message in data["contact_form_messages_list"]] #ALT: or is it data.get("contact_form_messages_list", []) instead of data["messages"] ???
    
        # return [ContactFormMessageModel(**message).to_schema() for message in data["messages"]] 
        # ^ TODO: RESEARCH: could add .to_schema() but ig its better practice to just return the model from the service layer, and then convert the model to schema in the route layer...????

# - submit new message in contact form
# TEMP: APPENDS message to the json file. my fruits_service.py saves the entire list again, which is not very efficient, and def not what i would do when i connect with dynamoDB. 
def save_message(message: ContactFormMessageModel) -> None:
    ENV_MODE = os.getenv("ENV_MODE", "aws").lower()
    if ENV_MODE == "aws":
        # Save to DynamoDB
        dynamodb = boto3.resource("dynamodb")
        table = dynamodb.Table(os.getenv("CONTACTFORMMESSAGES_TABLE_NAME"))

        try:
            item = message.to_dict()
            # Optionally add a UUID or timestamp if  don't already have one
            table.put_item(Item=item)

        except Exception as e:
            print(f"Error saving message to DynamoDB: {e}")
    else:
        with open(TEMP_DB_PATH, "r") as f:
            #load existing messages
            existing_data = json.load(f)
            messages = existing_data.get("contact_form_messages_list", [])
            
            #append new message to json file (since im not using an actual DB)
            messages.append(message.to_dict())
            
            # save updated list
            with open(TEMP_DB_PATH, "w") as f:
                json.dump({"contact_form_messages_list": messages}, f, indent=2)

# - delete messages
# TEMP: this is super temp since json files cant actually delete individual entries, since they're just text files. 
def delete_message(email: str, subject: str): #-> bool ???
    ENV_MODE = os.getenv("ENV_MODE", "aws").lower()
    if ENV_MODE == "aws":
        try:
            dynamodb = boto3.resource("dynamodb")
            table = dynamodb.Table(os.getenv("CONTACTFORMMESSAGES_TABLE_NAME"))

            # First, scan to find the message to delete
            response = table.scan()
            messages = response.get("Items", [])

            match = next(
                (msg for msg in messages if msg.get("email") == email and msg.get("subject") == subject),
                None
            )

            if not match:
                return False

            # Delete by primary key (must match the table’s schema)
            table.delete_item(Key={"id": match["id"]})
            return True

        except Exception as e:
            print(f"Error deleting message from DynamoDB: {e}")
            return False
    else:
        # TEMP int to check if message was deleted (aka if length changed)
        ogLength = 0 #TEMP
        
        # load all messages from JSON "database"
        with open(TEMP_DB_PATH, "r") as f:
            #load existing messages
            existing_data = json.load(f)
            messages = existing_data.get("contact_form_messages_list", [])
            ogLength = len(messages) #TEMP
        
        # remove message from json list
        # identify message to delete (TODO: maybe i should've included a generated id...? ex: in case i have duplicates of a message but still want to keep only one copy, etc)
        # ID for now: email + subject 
        # TEMP: i have to go thru the whole list to find the one i want to delete, then exclude it from my new message list, and then overwrite the JSON file with the new message list
        #       since json file can't delete individual entries
        #       even in the save_message I still have to get the list, add to list, and then overwrite the whole file with the new list
        # TEMP: So basically I have to filter out the messages instead of finding the exact entry, for now
        updated_message_list_excluding_deleted = [
            msg for msg in messages if not (msg["email"] == email and msg["subject"] == subject) # filters out (removes) any message
        ]
        
        # save updated list
        # TEMP: the way im implementing this is overwriting json file with my new message list
        with open(TEMP_DB_PATH, "w") as f:
            json.dump({"contact_form_messages_list": updated_message_list_excluding_deleted}, f, indent=2)
        
        # True = message successfully deleted, False = message not found and not deleted
        if ogLength != len(updated_message_list_excluding_deleted):
            return True
        return False