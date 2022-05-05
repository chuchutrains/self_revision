// Import library.
const express = require('express');
// Import file from other folder.
const bank_accs = require('../controllers/bank_acc');

const router = express.Router();
// Middleware function.
router.use((req, res, next) => {
    console.log('Request made to /BANK_ACC ROUTE');
    next();
});
// All routes in here are starting with /bank_acc.
router.get('/:uuid', bank_accs.readBankAcc);

// Export variable.
module.exports = router;