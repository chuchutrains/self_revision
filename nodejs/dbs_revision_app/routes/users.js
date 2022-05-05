// Import library.
const express = require('express');
// Import file from other folder.
const users = require('../controllers/users');

const router = express.Router();
// Middleware function.
router.use((req, res, next) => {
    console.log('Request made to /USERS ROUTE');
    next();
});
// All routes in here are starting with /users.
router.post('/register', users.createUser);
router.post('/login', users.readUser);

// Export variable.
module.exports = router;