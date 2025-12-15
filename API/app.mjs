//importación de librerias
import express from 'express';
import router from './routes/routes.mjs';
import dotenv from 'dotenv';
import colors from 'colors';

const app = express();
dotenv.config();

//variables del servidor
const port = process.env.API_PORT || 8080;
const ip = process.env.LOCAL_IP || 'localhost';

app.use(express.json());
app.use('/api', router);
app.set('json spaces', 2);

//configuración e inicialización del servidor nodejs
app.listen(port, ip, () => console.log(`listening port: ${port}, and ip: ${ip}`));
console.log(`url: ${ip}:${port}`.cyan);
