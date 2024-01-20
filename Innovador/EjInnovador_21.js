//Reportes ambientales


// Endpoint GET
app.get('/reporte-ambiental', (req, res) => {
  const { rangoFechas, tipoInformacion } = req.query;
  
  // Lógica para generar el informe basado en los parámetros
  const informe = `Informe para ${tipoInformacion} en el rango de fechas ${rangoFechas}`;
  
  res.send(informe);
});
