//
// Vista empleado
//

CREATE VIEW VistaEmpleadoHabilidades AS
SELECT E.Nombre, E.Salario, GROUP_CONCAT(H.Descripcion SEPARATOR ', ') AS Habilidades
FROM Empleados E
JOIN EmpleadoHabilidades EH ON E.ID = EH.ID_Empleado
JOIN Habilidades H ON EH.ID_Habilidad = H.ID_Habilidad
GROUP BY E.Nombre, E.Salario;
