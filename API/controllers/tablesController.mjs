import sqlite3 from 'sqlite3';
import { connect } from '../db/dbconnection.mjs';

//variables
let arrayColumns = ["hi", "bye"];

/**
*createTable is a function that connects with de database and create a new table
*@param [string] tableName - sqlite takes this param for create the table (name)
*@param [string[]] arrayColumns - sqlite takes this param for create the table with the strings for its columns (fields)
*@return [string] tableCreatedLog - afther that the function worked returns a string that returns an error or a string
*/
export async function createTable(tableName, arrayColumns){
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
		const query = `CREATE TABLE ${tableName} (${columns});`;

		//execution of query
		const db = await connect("../db/SalesPoint.db");
		db.run(query);
	} catch (error) { 
		console.log("error al crear la tabla: ", error); 
	}
}

await createTable("test", arrayColumns);
