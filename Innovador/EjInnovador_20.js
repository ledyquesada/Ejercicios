//Estado de la fauna


// Model
let estadoFauna = { poblacion: 1000, migracion: 'En curso' };

// Endpoint PUT
app.put('/estado-fauna', (req, res) => {
  const nuevoEstado = req.body;
  estadoFauna = { ...estadoFauna, ...nuevoEstado };
  res.json(estadoFauna);
});
