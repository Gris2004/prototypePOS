//importación de librerías
import sqlite3 from 'sqlite3';
import { open } from 'sqlite';

//habilitar el modo de depuración
sqlite3.verbose();

//función para conectar a base de datos
async function connectToDatabase() {
	//abriendo base de datos
	const db = await open({
		filename: './SalesPoint.db', //nombre de la base de datos
		driver: sqlite3.Database, //driver de sqlite
	});
	console.log("succesfull connection");
	return db;
}

//se llama a la función con un catch para caso de errores
await connectToDatabase().catch((err) => console.log(`error al conectar con la base de datos: ${err}`));
