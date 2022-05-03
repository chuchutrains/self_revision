// Youtube tutorial: https://www.youtube.com/watch?v=T2KjBiwYyBI&list=PL_cUvD4qzbkxZZyyuXa1xkWFhRB_NoQwl&index=1.

const express = require('express');
// const cookieParser = require('cookie-parser');
const session = require('express-session');

const usersRoute = require('./routes/users');
const postsRoute = require('./routes/posts');

const store = new session.MemoryStore();
const app = express();

// app.use(cookieParser());
app.use(session({
    secret: 'some secret', // Sign session cookie.
    cookie: {maxAge: 30000}, // 1s = 1000ms.
    saveUninitialized: false,
    store
}));
app.use(express.json());
app.use(express.urlencoded({extended: false}));

app.use((req, res, next) => {
    console.log(store);
    console.log(`${req.method} - ${req.url}`);
    next();
});

app.use('/users', usersRoute);
app.use('/posts', postsRoute);

app.listen(3000, () => {
    console.log('Server is running on Port 3000');
})

// const users = [
//     {name: 'Anson', age: 22},
//     {name: 'Kelvin', age: 21},
//     {name: 'Michelle', age: 22}
// ];

// const posts = [
//     {title: 'My favorite foods'},
//     {title: 'My favorite games'}
// ];

// app.get('/', (req, res) => {
//     res.send({
//         msg: 'Hello!',
//         user: {}
//     });
// });

// app.post('/', (req, res) => {
//     const user = req.body;
//     users.push(user);
//     res.status(201).send('Created User');
// });

// app.get('/users', (req, res) => {
//     res.status(200).send(users);
// });

// app.get('/users/:name', (req, res) => {
//     const {name} = req.params;
//     const user = users.find((user) => user.name === name);
//     if (user) res.status(200).send(user);
//     else res.status(404).send('Not Found');
// });

// app.get('/posts', (req, res) => {
//     const {title} = req.query;
//     if (title) {
//         const post = posts.find((post) => post.title === title);
//         if (post) res.status(200).send(post);
//         else res.status(404).send('Not Found');
//     }
//     res.status(200).send(posts);
// });

// function validateAuthToken(req, res, next) {
//     console.log('Inside Validate Auth Token');
//     const {authorization} = req.headers;
//     if (authorization && authorization==='123') {
//         next();
//     }
//     else {
//         res.status(403).send({msg: 'Forbidden. Incorrect Credentials'});
//     }
// }

// app.post('/posts', validateAuthToken, (req, res) => {
//     const post = req.body;
//     posts.push(post);
//     res.status(201).send(post);
// });

// // function validateCookies(req, res, next) {
// //     const {cookies} = req;
// //     if ('session_id' in cookies) {
// //         console.log('Session ID  Exists.');
// //         if (cookies.session_id  === '123456') next();
// //         else res.status(403).send({msg: 'Not Authenticated'});
// //     }
// //     else res.status(403).send({msg: 'Not Authenticated'});
// // }

// app.get('/signin', (req, res) => {
//     res.cookie(`session_id`, '123456');
//     res.status(200).json({msg: 'Logged In.'});
// });

// // app.get('/protected', validateCookies, (req, res) => {
// //     res.status(200).json({msg: 'You are authorized!'});
// // });

// app.post('/login', (req, res) => {
//     console.log(req.sessionID);
//     const {username, password} = req.body;
//     if (username && password) {
//         // User logged in.
//         if (req.session.authenticated) {
//             res.json(req.session);
//         }
//         else {
//             if (password === '123') {
//                 req.session.authenticated = true;
//                 req.session.user = {username, password};
//                 res.json(req.session);
//             }
//             else {
//                 res.status(403).json({msg: 'Bad Cedentials'});
//             }
//         }
//     }
//     else {
//         res.status(403).json({msg: 'Bad Cedentials'});
//     }
// });

