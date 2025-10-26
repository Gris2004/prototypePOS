// Importing libraries
import path from 'path';
import dotenv from 'dotenv';
import { fileURLToPath } from 'url';

//configure dotenv
const __dirname = path.dirname(fileURLToPath(import.meta.url));
const envPath = path.resolve(__dirname, "../../.env");
dotenv.config({path: envPath});

/**
 *dbPath takes the value from the .env and create an absolute path for open the db
 *@return [path.resolve] dbRoute - the variable for open the database from any directory
*/
export function dbPath() {
    //dirname for an absolute path
    const _dirname = path.dirname(`${process.env.DB_PATH}`);
}
console.log(dbPath());
console.log(envPath);
