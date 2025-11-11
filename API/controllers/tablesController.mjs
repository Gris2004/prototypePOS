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
     * @return {Promise} [resolve (rows), reject (error)] - returns a fields array or an error
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
     * @return {Promise} [resolve, reject] - the name of created table or an error
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

    /**
     * takes a table name and delete the table from the database
     * @param {string} tableName - this param stores the name of the table for delete the table 
     * @return {Promise} [resolve(string) reject(error)] - returns a string whith the table name deleted or an error */
    dropTable(tableName) {
        const query = `DROP TABLE ${tableName}`;
        return new Promise((resolve, reject) => {
            db.run(query, (err) => {
                if(err) reject(err);
                else resolve(`the table ${tableName} was deleted`);
            });
        });
    }

    /**
     * describes the table from the tableName param
     * @param {string} tableName - the tables's name
     * @return {string[]} [err, fields] - return the fields or an error
     * */
    describeTable(tableName){
        const query = `PRAGMA table_info(${tableName})`;
        return new Promise((resolve, reject) => {
            db.all(query, (err, fields) => {
                if(err) reject(err);
                else resolve(fields);
            });
        });
    }

    /**
     * inserts a new record in the tableName with the array of fields for the insertion
     * @param {string} tableName - the table's name
     * @param {string[]} array - the values for the record
     * @return {Promise} (resolve, reject) - returns the tablename and the records or an error
     * */
    insertRecord(tableName, array){
        //array param in a string
        const values = array.join(", ");
        
        //table fields in a string in string[] format
        const fieldsDescribe = [];
        this.describeTable(tableName).then(result => {
            fieldsDescribe = result;
        }).catch(error => {
            console.error("error message: ", error);
        });
        for(let i = 0; i < fieldsDescribe.length(); i++){
            console.log(`${i}\n`);
        }
    }
}

const tableController = new TablesController(db);

//example of the execution with functions that returns a Promise
/*tableController.describeTable('test').then(result => {
    console.log(result);
}).catch(error => {
    console.error("error message: ", error);
});*/

tableController.insertRecord('test', ['hi', 'bye']);
