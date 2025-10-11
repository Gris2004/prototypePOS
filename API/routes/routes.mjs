import { Router } from 'express'

var router = Router();

//endpoint para consultar las tablas
router.get('/tables/consult', async(req, res) => {
    res.json({"message": "this is the consult endpoint to watch the tables"})
});

//endpoint para crear un registro
router.post('/tables/create', async(req, res) => {
    res.json({"message": "this is the endpoint to create a field in any table "})
});

router.delete('/tables/delete', async(req, res) => {
    res.json({"message": "this is the endpoint to delete a field in any table width an id"})
});

router.post('/tables/update', async(req, res) => {
    res.json({"message": "this is the endpoint to update a field in any table with an id or an script"})
});

export default router
