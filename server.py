const express = require('express');
const app = express();

app.get('/api', (req, res) => {
    res.json({ message: "Hello from VM 1 (Microservice Server)!" });
});

app.listen(5000, '0.0.0.0', () => {
    console.log("Server running on port 5000");
});
