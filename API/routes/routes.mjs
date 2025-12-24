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

router.post('/tables/create', async(req, res) => {
    const { name, array } = req.body;
    res.json({"message": await tableController.createTable(name, array)});
});

router.post('/records/insert', async(req, res) => {
    const { name, array } = req.body;
    res.json({
        "message": await tableController.insertRecord(name, array)
    });
});
export default router
