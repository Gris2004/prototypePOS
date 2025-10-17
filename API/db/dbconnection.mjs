//importando librerías
import sqlite3 from 'sqlite3';

//activando modo de depuración
sqlite3.verbose();

//inicialización de Database
const db = new sqlite3.Database('SalesPoint.db');
