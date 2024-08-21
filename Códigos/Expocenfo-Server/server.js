const express = require('express');
const app = express();
const port = 3000;

// Middleware para parsear JSON
app.use(express.json());

// Ruta para recibir los datos desde el microcontrolador
app.post('/send-url', async (req, res) => {
    const url = req.body.url;

    if (url) {
        console.log(`URL recibida: ${url}`);

        // Importa y abre la URL en el navegador de manera dinámica
        const open = await import('open');
        open.default(url);

        res.status(200).send('URL recibida y procesada.');
    } else {
        res.status(400).send('No se recibió ninguna URL.');
    }
});

app.listen(port, () => {
    console.log(`Servidor escuchando en http://localhost:${port}`);
});
