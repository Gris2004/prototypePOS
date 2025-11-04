//importing dependencies
import { connect } from '../db/dbconnection.mjs';
import { dbPath } from '../db/dbUtils.mjs';
import dotenv from 'dotenv';

//db const that will keep open in each transaction, when the client closes, the database will too
const db = connect(dbPath);
dotenv.config();

/**
 * fetchData show the rows from the selected table
 * @param [string] tableName - the table name for execute the consult
 * @return [string] [rows, fields] - the rows and fieds from the table
 * */

export function fetchData (tableName) {
    const query = `SELECT * FROM ${tableName}`;
    const rows = db.prepare(query).all;
    return rows;
}

console.log(fetchData('testTable'));
