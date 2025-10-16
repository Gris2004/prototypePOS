//importación de librerías
import sqlite3 from 'better-sqlite3';
import { open } from 'better-sqlite3';

//variables
let columsNameArray = []

//habilitar el modo de depuración
sqlite3.verbose();

/**
*connectToDatabase es una función que te permite conectarte al archivo SalesPoint.db
*/
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

//función para crear tablas
/**
*create tables sirve para crear tablas con2 parametros
*@param {string} ableName - el nombre de la tabla
*@param {string arry} columnsArray - arreglo de las columnas a crear
*/
async function createTable(tableName, columnsArray){
	if (!Array.isArray(columnsArray) || columnsArray.length === 0){
		throw new Error(console.log("El arreglo de columnas no puede estar vacia"));
	}	
	
	if (!/^[a-zA-Z0-9_]+$/.test(tableName)){
		throw Error(console.log("Nombre de tabla no valido"));
	}
	const columns = columnsArray.join(", ") //converte "id", "integer" en "name TEXT" en "id INTEGER, name TEXT"
	try{
		const db = await connectToDatabase();	
		await db.run(`CREATE TABLE ${tableName} (${columns});`);
	} catch (error) {
		console.log("error al crear la tabla", error);
	}
}

//se llama a la función con un catch para caso de errores
await connectToDatabase().catch((err) => console.log(`error al conectar con la base de datos: ${err}`));

//creación de una tabla de prueba
columsNameArray = ["test1 VARCHAR(256)", "test2 INT(11)"];
await createTable("test", columsNameArray);
