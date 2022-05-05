// DBS Youtube tutorial: https://www.youtube.com/watch?v=l8WPWK9mS5M.
// Anson Youtube tutorial: https://www.youtube.com/watch?v=T2KjBiwYyBI&list=PL_cUvD4qzbkxZZyyuXa1xkWFhRB_NoQwl&index=1.

// Import libraries.
const express = require('express');
const session = require('express-session');
// Import files from other folders.
const usersRoutes = require('./routes/users');
const bankAccRoutes = require('./routes/bank_acc');

const app = express();
const PORT = 5000;
// Handle request body.
app.use(express.json());
app.use(express.urlencoded({extended: false}));
// Middleware function.
app.use((req, res, next) => {
    console.log(`${req.method} - ${req.url}`);
    next();
});
// Routes.
app.get('/home', (req, res) => res.send('dbs revision app home page.'));
app.use('/users', usersRoutes);
app.use('/bank_acc', bankAccRoutes);
app.listen(PORT, () => {
    console.log(`Server is running on Port: http://localhost.${PORT}`);
});

// Session and cookies.
const store = new session.MemoryStore();
app.use(session({
    secret: 'some secret', // Sign session cookie.
    cookie: {maxAge: 30000}, // 1s = 1000ms.
    saveUninitialized: false,
    store
}));
