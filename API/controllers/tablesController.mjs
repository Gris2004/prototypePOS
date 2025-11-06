//importing dependencies
import { dbPath, db } from '../db/dbUtils.mjs';
import dotenv from 'dotenv';

//db const that will keep open in each transaction, when the client closes, the database will too
dotenv.config();

//variables
var arrayColumns = []

/**
 * fetchData show the rows from the selected table
 * @param [string] tableName - the table name for execute the consult
 * @return [string] [rows, fields] - the rows and fieds from the table
 * */

export function fetchData (tableName) {
    try{
        //query for execute the consult
        const query = `SELECT * FROM ${tableName}`; 

        //promise that returns rows from the 
        return new Promise((resolve, reject) => {
            db.all(query, (err, rows) => {
                if (err) reject(err);
                else resolve(rows);
            });
        });
    } catch (error){
        console.error("Error Message: ", error);
    }
}

/**
 *create a table
 * @param {string} tableName - the table's name
 * @param {array[string]} array - the fields for the table
 * */
export function createTable (tableName, array) {
    try {
        const columns = array.join(", ");
        const query = `CREATE TABLE ${tableName} (${columns})`;
        db.run(query);
    } catch (error) {
        console.error("error message: ", error);
    }
}

//call function fetchData for a test
fetchData('testTable').then(rows => {
    console.log(rows);
});

createTable('test2', ['test1', 'test2']);
