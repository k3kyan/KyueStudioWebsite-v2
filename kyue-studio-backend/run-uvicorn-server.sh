#!/bin/bash

# check that uvicorn is installed
# should only be installed in venv, so only will show version if venv is running
# uvicorn --version


# run uvicorn server
# allows access to endpoints locally (or something)
# make sure venv is running (will show in terminal) when activating this command
uvicorn main:app --reload
echo "Running uvicorn server..."