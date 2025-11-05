// Importing libraries
import path from 'path';
import dotenv from 'dotenv';
import sqlite3 from 'sqlite3';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
//configure dotenv
const envPath = path.resolve(__dirname, "../../.env");
dotenv.config({path: envPath});

/**
 *dbPath takes the value from the .env and create an absolute path for open the db
 *@return [path.resolve] dbRoute - the variable for open the database from any directory
*/
export const dbPath = path.resolve(__dirname, "./SalesPoint.db");
export const db = new sqlite3.Database(dbPath);
console.log(db);
