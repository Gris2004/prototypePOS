//importación de librerias
import express from 'express';

const app = express();

//variables del servidor
const port = 8080;
const server = 'localhost';

//endpoint para consultar las tablas
app.get('/tables/consult', async(req, res) => {
    res.json({"message": "this is the consult endpoint to watch the tables"})
});

//endpoint para crear un registro
app.post('/tables/create', async(req, res) => {
    res.json({"message": "this is the endpoint to create a field in any table "})
});

app.delete('/tables/delete', async(req, res) => {
    res.json({"message": "this is the endpoint to delete a field in any table width an id"})
});

app.post('/tables/update', async(req, res) => {
    res.json({"message": "this is the endpoint to update a field in any table with an id or an script"})
});
//configuración e inicialización del servidor nodejs
app.listen(port, server);
