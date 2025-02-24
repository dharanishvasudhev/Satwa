import express from 'express';
import pool from './dbConfig.js';



const app = express();
const PORT = 3001;


app.use(express.json());

// Sample endpoint to fetch data
app.get('/data', async (req, res) => {
    try {
        const [rows] = await pool.query('SELECT * FROM waste_weights');

        res.json(rows);
    } catch (error) {
        console.error(error); // Log the error for debugging
        res.status(500).json({ error: 'Database query failed', details: error.message });

    }
});

app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
