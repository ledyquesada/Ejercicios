//
// Programación Java
//

-- Agregar habilidades
INSERT INTO Habilidades (ID_Habilidad, Descripcion) VALUES
(1, 'Programación Java'),
(2, 'Diseño Gráfico');

INSERT INTO EmpleadoHabilidades (ID_Empleado, ID_Habilidad) VALUES
(1, 1), -- Juan Pérez tiene la habilidad de Programación Java
(2, 2); -- María González tiene la habilidad de Diseño Gráfico

//Encontrando

SELECT E.Nombre
FROM Empleados E
JOIN EmpleadoHabilidades EH ON E.ID = EH.ID_Empleado
JOIN Habilidades H ON EH.ID_Habilidad = H.ID_Habilidad
WHERE H.Descripcion = 'Programación Java';



