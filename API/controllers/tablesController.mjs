import sqlite3 from 'sqlite3';
import connect from '../db/dbconnection.mjs';

//variables
let arrayColumns = ["name VARCHAR(256)", "bye VARCHAR(256)"];
const db = connect(dbDirectory);

/**
*createTable is a function that connects with de database and create a new table
*@param [string] tableName - sqlite takes this param for create the table (name)
*@param [string[]] arrayColumns - sqlite takes this param for create the table with the strings for its columns (fields)
*@param [string] dbDirectory - takes the directory of the db file
*@return [string] tableCreatedLog - afther that the function worked returns a string that returns an error or a string
*/
export async function createTable(dbDirectory, tableName, arrayColumns){
	//validación de arreglos y el nombre de la tabla
	if (!Array.isArray(arrayColumns) || arrayColumns.length === 0) {
		throw new Error("Arreglo no valido o vacio");
	}
	if (!/^[a-zA-Z0-9_]+$/.test(tableName)){
		throw new Error("tableName invalid");
	}	
	//try catch for create the table
	try {
		//variables for the query execute
		const columns = arrayColumns.join(", ");
		const query = `CREATE TABLE IF NOT EXISTS ${tableName} (${columns});`;

		//execution of query
		db.run(query);
	} catch (error) { 
		console.log("error al crear la tabla: ", error); 
	}
}

/**
*fetchData recovers a json that contains the data returned for the query 
*@param [string] dbDirectory - stores a value for open the file.db
*@param [string] tableName - table name for get the data of the table
*@returns [string] data - string that takes a json of the query
*/
export async function fetchData(dbDirectory, tableName){
	try{
		const query = `SELECT * FROM ${tableName}`;
		const [rows, fields] = db.run(query);
		return [rows, fields];
		db.close();
	} catch (error) {
		console.log("message: directory or tableName is invalid", error);
	}
}

console.log(await createTable("../db/SalesPoint.db", "test", arrayColumns));
console.log(await fetchData("../db/SalesPoint.db", "test"));
