import { Router } from 'express'
import { db } from '../db/dbutils.mjs'
import TablesController from '../controllers/tablesController.mjs'

var router = Router();
const tableController = new TablesController(db);
//endpoint to fetchData
router.get('/tables/consult', async(req, res) => {
    const { name } = req.query;
    res.json({"message": await tableController.fetchData(name)});
});

//endpoint to describeTable
router.get('/tables/describe', async(req, res) => {
    //the table's Name
    const { name } = req.query;
    
    //executing the function and whoing the output
    res.json({"message": await tableController.describeTable(name)});
});

//endpoint to createTable
router.post('/tables/create/name/values', async(req, res) => {
    const name = req.query.name;
    const values = req.query.values;

    res.json({"message": await tablesController.createTable(name, values)});
});

export default router
