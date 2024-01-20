//Lista de areas de conservacion


// Model
const areasConservacion = [
  { nombre: 'Área 1', descripcion: 'Descripción 1', hectareas: 100 },
  { nombre: 'Área 2', descripcion: 'Descripción 2', hectareas: 150 },
];

// Endpoint GET
app.get('/areas-conservacion', (req, res) => {
  res.json(areasConservacion);
});
