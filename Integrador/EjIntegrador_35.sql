// 
// Contar empleados
//

SELECT P.Nombre, COUNT(A.ID_Empleado) AS TotalEmpleados
FROM Proyectos P
LEFT JOIN Asignaciones A ON P.ID = A.ID_Proyecto
GROUP BY P.Nombre;

