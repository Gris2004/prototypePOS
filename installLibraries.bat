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
	pnpm install
) else (
	echo no hay archivo de package.json
	echo se realizará el siguiente comando: npm init -y
	pnpm init
	pnpm install -D eslint
	pnpm install -S nodemon
	pnpm install -S express
	pnpm install -S better-sqlite3
)

echo.
echo Listo
pause
