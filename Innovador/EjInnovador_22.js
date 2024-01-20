//Autenticación

// Uso de JWT para autenticación
const jwt = require('jsonwebtoken');

// Endpoint protegido
app.post('/observaciones', validarToken, (req, res) => {
  // Lógica para agregar nueva observación
  res.status(201).json({ mensaje: 'Observación registrada exitosamente' });
});

function validarToken(req, res, next) {
  const token = req.headers.authorization;

  if (!token) {
    return res.status(401).json({ error: 'Token no proporcionado' });
  }

  try {
    const usuario = jwt.verify(token, 'TU_SECRETO');
    req.usuario = usuario;
    next();
  } catch (error) {
    res.status(401).json({ error: 'Token inválido' });
  }
}
