// Youtube tutorial: https://www.youtube.com/watch?v=l8WPWK9mS5M.

import express from "express";
import bodyParser from 'body-parser';
import usersRoutes from './routes/users.js'

const app = express();
const PORT = 5000;

app.use(bodyParser.json());
app.use('/users', usersRoutes);

app.get('/', (req, res) => res.send('Hello from Homepage.'));

app.listen(PORT, () => console.log(`Server Running on port: http://localhost:${PORT}`))