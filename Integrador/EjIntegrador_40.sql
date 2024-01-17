//
// Habilidad comun
//
  
SELECT H.Descripcion
FROM Habilidades H
JOIN EmpleadoHabilidades EH ON H.ID_Habilidad = EH.ID_Habilidad
GROUP BY H.Descripcion
ORDER BY COUNT(EH.ID_Empleado) DESC
LIMIT 1;
