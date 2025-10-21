import { Router } from 'express'
import { connect } from '../db/dbconnection.mjs'

var router = Router();

//endpoint para consultar las tablas
router.get('/tables/consult/:name', async(req, res) => { 
	const name = req.params.name;
	res.json({"message": `${name}`});
});

//endpoint para crear un registro
router.post('/tables/create', async(req, res) => {
    res.json({"message": "this is the endpoint to create a row in any table "});
});

router.delete('/tables/delete', async(req, res) => {
    res.json({"message": "this is the endpoint to delete a row in any table width an id"});
});

router.post('/tables/update', async(req, res) => {
    res.json({"message": "this is the endpoint to update a row in any table with an id or an script"});
});

export default router
