#!/bin/bash

APP_NAME=kyue-studio-website-v3

npm create vite@latest "$APP_NAME" -- --template react
cd "$APP_NAME"
npm install
npm install react-router-dom

echo "Created project successfully"

# make scripts executable
# chmod +x createproject.sh runstart.sh

# run script to create project
# ./createproject.sh

# run project/test/etc scripts in project folder
# cd kyue-studio-website-v3
# ./runstart.sh

# USE BASH!! git bash terminal in vs code