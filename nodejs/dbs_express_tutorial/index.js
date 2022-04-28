// Youtube tutorial: https://www.youtube.com/watch?v=l8WPWK9mS5M.
// 1. To run, open up the terminal and run "npm start".
// 2. Open up a browser and go to http://localhost:5000.
// 3. Use Postman app to do CRUD operation.

import express from 'express';
import bodyParser from 'body-parser';
import usersRoutes from './routes/users.js'

const app = express();
const PORT = 5000;

app.use(bodyParser.json());
app.use('/users', usersRoutes);
app.get('/', (req, res) => res.send('Hello from Homepage.'));
app.listen(PORT, () => console.log(`Server Running on port: http://localhost:${PORT}`));
