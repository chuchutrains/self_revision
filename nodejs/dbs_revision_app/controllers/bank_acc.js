// Import library.
const jwt = require('jsonwebtoken');
// require("dotenv").config();
// Import file from other folder.
const db = require('../database_config');

const readBankAcc = (req, res) => {
    const token = req.body.token;
    const decoded = jwt.verify(token, process.env.TOKEN_KEY);
    const timeNow = Math.floor(Date.now()/1000)
    if (decoded.exp < timeNow) {
        return res.status(401).send("Invalid Token."); // 401 Unauthorized
    }
    return res.status(200).send(`Welcome ${req.body.user_id}`);
};

// Export functions.
module.exports = {readBankAcc};