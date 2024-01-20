// Observación ambiental

// Model
const observaciones = [];

// Endpoint POST
app.post('/observaciones', (req, res) => {
  const nuevaObservacion = req.body;
  observaciones.push(nuevaObservacion);
  res.status(201).json(nuevaObservacion);
});
