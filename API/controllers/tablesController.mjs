//importing dependencies
import { dbPath, db } from '../db/dbUtils.mjs';
import dotenv from 'dotenv';

//db const that will keep open in each transaction, when the client closes, the database will too
dotenv.config();

/**
 * fetchData show the rows from the selected table
 * @param [string] tableName - the table name for execute the consult
 * @return [string] [rows, fields] - the rows and fieds from the table
 * */

export function fetchData (tableName) {
    try{
        //reading all users
        const query = `SELECT * FROM ${tableName}`;
        const rows = db.run(query);
        return rows;
    } catch (error){
        console.error("Error Message: ", error);
    }
}

console.log(fetchData('testTable'));
