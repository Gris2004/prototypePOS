//importando librerías
import sqlite3 from 'sqlite3';

//activando modo de depuración
sqlite3.verbose();

/**
*connect is a function that connects with SalesPointDb
*No params
*@return sqlite3.Database object
*/
export async function connect(){
	const db = new sqlite3.Database('./api/db/SalesPoint.db');
	return db
}
