//DAtos meteorológicos


// Uso de axios para hacer solicitudes HTTP
const axios = require('axios');

// Endpoint GET
app.get('/datos-meteorologicos', async (req, res) => {
  const { latitud, longitud } = req.query;
  
  try {
    const response = await axios.get(`https://api.openweathermap.org/data/2.5/weather?lat=${latitud}&lon=${longitud}&appid=TU_API_KEY`);
    const datosMeteorologicos = response.data;
    res.json(datosMeteorologicos);
  } catch (error) {
    res.status(500).json({ error: 'Error al obtener datos meteorológicos' });
  }
});
