#!/usr/bin/env bash

echo "Configuring the Python virtual environment..."

if [ ! -d "env" ]; then
    echo "Environment not found. Creating..."
    python3 -m venv env
    echo "Virtual environment created."
else
    echo "The environment is already configured."
fi

#enable the scripts in the env and install the python libraries
envConfig(){
    echo "installing libraries for python"
    source env/bin/activate
    python3 -m pip install --upgrade pip
    python3 -m pip install -r requirements.txt
}

envConfig

if [ -f "./package.json" ]; then
    npm install
else
    echo "package.json not found. adding node.js libraries ..."
    npm init -y
    #update npm
    npm install -g npm@11.6.4
	
    #add libraries
    npm add -D eslint
    npm add -D dotenv
	npm add -S nodemon
	npm add -S express
	npm add -S sqlite3
    npm add -S path
    npm add -S colors

fi
