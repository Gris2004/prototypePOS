import { Router } from 'express'
import { db } from '../db/dbutils.mjs'
import TablesController from '../controllers/tablesController.mjs'

var router = Router();
const tableController = new TablesController(db);

//endpoint to fetchData
router.get('/tables/consult/:name', async(req, res) => {
    const name = req.params.name;
    res.json({"message": await tableController.fetchData(name)});
});

//endpoint to describeTable
router.get('/tables/describe/:name', async(req, res) => {
    //the table's Name
    const name = req.params.name;
    
    //executing the function and whoing the output
    res.json({"message": await tableController.describeTable(name)});
});

//endpoint to createTable
routes.post('/tables/create/name/values', async(req, res) => {
    const name = req.query.name;
    const values = req.query.values;

    res.json({"message": await tablesController.createTable(name, values)});
});

/*
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
});*/

export default router
