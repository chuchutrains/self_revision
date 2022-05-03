// Import libraries.
const {v4: uuidv4} = require('uuid');
const {check, validationResult} = require('express-validator');
// Import file from other folder.
const db = require('../database_config');

const createUser = (req, res) => {
    const user = req.body;
    res.send(`User with the name ${uuidv4()} added to the database!`);
}

// Export functions.
module.exports = {createUser};