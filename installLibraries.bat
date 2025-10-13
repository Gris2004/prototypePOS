@echo off
REM configuración de entorno de python
echo configurando entorno de python

if not exist env (
	python.exe -m venv env
)

env\Scripts\python.exe -m pip install --upgrade pip
env\Scripts\python.exe -m pip install -r requirements.txt
echo.

REM configuración de librerías de node.js
echo instalando dependencias de node.js
if exist package.json (
	npm install
) else (
	echo no hay archivo de package.json
	echo se realizará el siguiente comando: npm init -y
	npm init -y
	npm install -D eslint
	npm install -S nodemon
	npm install -S express
	npm install -S sqlite3
	npm install -S sqlite
)

echo.
echo Listo
pause
