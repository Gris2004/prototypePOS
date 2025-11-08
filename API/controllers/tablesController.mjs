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
}

//db const that will keep open in each transaction, when the client closes, the database will too
dotenv.config();
