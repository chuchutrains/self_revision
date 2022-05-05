// Import libraries.
const {check, validationResult} = require('express-validator');
const {v4: uuidv4} = require('uuid');
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');
require("dotenv").config();
// Import file from other folder.
const db = require('../database_config');

const createUser = [[
    // https://express-validator.github.io/docs/validation-chain-api.html.
    check('user_id')
        .notEmpty().withMessage('User ID cannot be empty.')
        .matches(/^[A-Za-z0-9]+$/).withMessage("Special characters not allowed in user ID."),
    check('pin')
        .notEmpty().withMessage('Pin cannot be empty.')
        .isInt().withMessage('Only numbers allowed in pin.')
        .isLength({min: 6, max: 9}).withMessage('The PIN length should range from 6 to 9 digits.'),
    check('phone_number')
        .notEmpty().withMessage('Phone number cannot be empty.')
        .isInt().withMessage('Only numbers allowed in phone number.')
        .isLength({min: 8, max: 8}).withMessage('Invalid phone number.'),
    check('email')
        .notEmpty().withMessage('Email address cannot be empty.')
        .isEmail().withMessage('Invalid email address.')
], async (req, res) => {
    const errors = validationResult(req);
    // check() validation error.
    if (!errors.isEmpty()) {
        return res.status(400).json({errors: errors.array()}); // 400 Bad Request.
    }
    
    // no check() validation error.
    const {user_id, pin, phone_number, email} = req.body;
    // Generate salt to hash the pin.
    const salt = await bcrypt.genSalt(10);
    const hashedPin = await bcrypt.hash(pin, salt);
    try {
        await db.promise().query(`
            INSERT INTO USERS VALUES(
                '${uuidv4()}',
                '${user_id}',
                '${hashedPin}',
                '${phone_number}',
                '${email}'
            )
        `);
        return res.status(201).send({msg: 'User created successfully.'}); // 201 Created.
    } catch (err) { // SQL query error.
        if (err['code'] === 'ER_DUP_ENTRY') {
            const sqlErrMsg = err['sqlMessage'];
            // Duplicate entry '???' for key 'users.???_UNIQUE'
            const field = sqlErrMsg.substring(sqlErrMsg.indexOf("'u")+7, sqlErrMsg.indexOf("E'")-6);
            const colKeyMapping = {
                'user_id': 'User ID',
                'pin': 'Pin',
                'phone_number': 'Phone number',
                'email': 'Email address'
            };
            return res.status(400).send(colKeyMapping[field] + ' has been used.'); // 400 Bad Request.    
        }
        console.log(err['sqlMessage']);
        return res.status(500).send(err['sqlMessage']); // 500 Internal Server Error.
    }
}];

const readUser = [[
    check('user_id')
        .notEmpty().withMessage('User ID cannot be empty.')
        .matches(/^[A-Za-z0-9]+$/).withMessage("Special characters not allowed in user ID."),
    check('pin')
        .notEmpty().withMessage('Pin cannot be empty.')
        .isInt().withMessage('Only numbers allowed in pin.')
        .isLength({min: 6, max: 9}).withMessage('The PIN length should range from 6 to 9 digits.')
], async (req, res) => {
    const errors = validationResult(req);
    // check() validation error.
    if (!errors.isEmpty()) {
        return res.status(400).json({errors: errors.array()}); // 400 Bad Request.
    }

    // no check() validation error.
    const {user_id, pin} = req.body;
    const loginErrMsg = 'Your User ID or PIN is incorrect. Please try again.';
    var userResult = await db.promise().query(`
        SELECT * FROM USERS
        WHERE user_id = '${user_id}'
    `);
    userResult = userResult[0];
    // User not found.
    if (userResult.length === 0) {
        return res.status(403).send(loginErrMsg); // 403 Forbidden.
    }
    const hashedPin = userResult[0]['pin'];
    const validPassword = await bcrypt.compare(pin, hashedPin);
    // Wrong password.
    if (!validPassword) {
        return res.status(403).send(loginErrMsg); // 403 Forbidden.
    }
    // Login successfully.
    // Create token.
    const token = jwt.sign(
        {username: user_id, pin},
        process.env.TOKEN_KEY, // Get constant var from .env file.
        {expiresIn: "2h"}
    );
    // Save user token.
    var user = {
        'uuid': userResult[0]['uuid'],
        'user_id': user_id,
        'phone_number': userResult[0]['uuid'],
        'email': userResult[0]['email'],
        'token': token
    };
    res.status(200).send(user); // 200 OK.
    // res.redirect('/bank_acc/welcome');
    
    // @TODO: Implement session and cookies?
}];

// Export functions.
module.exports = {createUser, readUser};