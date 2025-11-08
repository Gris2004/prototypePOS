//importing dependencies
import { dbPath, db } from '../db/dbUtils.mjs';
import dotenv from 'dotenv';

/**
 * this class contains the functions to manage the database easier than use the sqlite3 functions 
 * */
class TablesController { 
    /**
     * @constructor
     * @param {sqlite3.Database} db - takes a const which store a sqlite3.Database object*/
    constructor(db){
        this.db = db;
    }

    /**
     * fetchData show the rows from the selected table
     * @param {string} tableName - the table name for execute the consult
     * @return {string} [rows, fields] - the rows and fieds from the table
     * */
    fetchData (tableName) {
        //query for execute the consult
        const query = `SELECT * FROM ${tableName}`; 
        
        //promise that returns rows from the 
        return new Promise((resolve, reject) => {
            db.all(query, (err, rows) => {
                if (err) reject(err);
                else resolve(rows);
            });
        });
    }

    /**
     * takes a tableName and a columnsArray to create a new table in sqlite3 db
     * @param {string} tableName - the table's name
     * @param {string[]} array - the fields for the table
     * */
    createTable (tableName, array) {
        //preparing the statement
        const columns = array.join(", ");
        const query = `CREATE TABLE ${tableName} (${columns})`;

        return new Promise((resolve, reject) => {
            db.run(query, (err) => {
                if(err) reject(err);
                else resolve(`table: ${tableName} was created succefuly with the fields: ${columns}`);
            });
        });
    }
}

//db const that will keep open in each transaction, when the client closes, the database will too
dotenv.config();
