// Import file from other folder.
const db = require('../database_config');

const readBankAcc = (req, res) => {
    const frontendUserUUID = req['url'].substring(1);
    return res.status(200).send(frontendUserUUID); 
};

// Export functions.
module.exports = {readBankAcc};