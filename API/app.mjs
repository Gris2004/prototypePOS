//importación de librerias
import express from 'express';
import router from './routes/routes.mjs'

const app = express();

//variables del servidor
const port = process.env.port || 8080;
const ip = process.env.ip || 'localhost';

app.use('/api', router);
app.set('json spaces', 2);


//configuración e inicialización del servidor nodejs
app.listen(port, ip);
