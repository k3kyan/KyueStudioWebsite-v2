#!/bin/bash

# ONLY RUN THIS SCRIPT IF VENV AND UVICORN ARE NOT RUNNING ALREADY 

# running on git bash terminal
# run the virtual environment, need to run for fastapi and uvicorn to work
# (if on cmh command prompt, use "fastapi-venv/Scripts/activate.bat(?)" instead)
source fastapi-venv/Scripts/activate
echo "Running virtual environment..."


# install fastAPI (only needed once at initialization)
# pip install fastapi

# install pydantic (only needed once at initialization)
# pip install pydantic
# check that pydantic is installed
# how ??? idk

# install uvicorn (only needed once at initialization)
# pip install uvicorn

# check that uvicorn is installed
# should only be installed in venv, so only will show version if venv is running
# uvicorn --version


# run uvicorn server
# allows access to endpoints locally (or something)
# make sure venv is running (will show in terminal) when activating this command
uvicorn main:app --reload
echo "Running uvicorn server..."







# make scripts executable
# chmod +x run-backend.sh run-uvicorn-server.sh runvenv.sh 

# run script to create project
# ./createproject.sh
# ./run-backend.sh 
# ./run-uvicorn-server.sh 
# ./runvenv.sh 

# USE BASH!! git bash terminal in vs code