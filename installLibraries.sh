#!/usr/bin/env bash

# installing python3-tk
echo "It's going to install python3-tk with apt. Do you want to continue? Y/n"
read opt
if [[ "$opt" =~ ^[Yy]$ ]]; then
    sudo apt install python3-tk -y
fi

# installing nodejs and npm
echo "It's going to install nodejs and npm. Do you want to continue? Y/n"
read opt
if [[ "$op" =~ ^[Yy]$ ]]; then
    sudo apt install nodejs npm -y
fi

echo "Configuring the Python virtual environment..."

if [ ! -d "env" ]; then
    echo "Environment not found. Creating..."
    python3 -m venv env
    echo "Virtual environment created."
else
    echo "The environment is already configured."
fi

# enable env and install python libs
envConfig(){
    echo "Installing Python libraries..."
    source env/bin/activate
    python3 -m pip install --upgrade pip
    python3 -m pip install -r requirements.txt
}

envConfig

# node dependencies
if [ -f "./package.json" ]; then
    npm install
else
    echo "package.json not found. Initializing npm project..."
    npm init -y
    npm install -g npm@latest

    # add libraries
    npm install -D eslint dotenv nodemon
    npm install express sqlite3 path colors
fi

