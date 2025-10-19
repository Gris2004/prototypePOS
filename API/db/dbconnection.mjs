//importando librerías
import sqlite3 from 'sqlite3';

//activando modo de depuración
sqlite3.verbose();

/**
*connect is a function that connects with SalesPointDb
*@param [string] - FileDirectory - for open the database
*@return sqlite3.Database object
*/
export async function connect(fileDirectory){
	const db = new sqlite3.Database(fileDirectory);
	return db
}
