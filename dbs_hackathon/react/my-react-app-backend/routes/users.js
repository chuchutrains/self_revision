import express from 'express';
import { createUser, getUsers, getUser, updateUser, deleteUser } from '../controllers/users.js';

const router = express.Router();

// All routes in here are starting with /users.
router.post('/', createUser);

router.get('/', getUsers);

router.get('/:id', getUser);

router.patch('/:id', updateUser);

router.delete('/:id', deleteUser);

export default router;