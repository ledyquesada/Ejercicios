--
-- Tres proyectos
--

--Se asume que ya realizon los ajustes en la tabla EmpleadosProyectos

--Ahora encontramos empleados

WITH EmpleadosProyectos AS (
    SELECT ED.ID_Empleado, COUNT(DISTINCT ED.ID_Proyecto) AS CantidadProyectos
    FROM EmpleadosDepartamentos ED
    GROUP BY ED.ID_Empleado
    HAVING COUNT(DISTINCT ED.ID_Proyecto) >= 3
)
SELECT E.ID, E.Nombre, EP.CantidadProyectos,
       GROUP_CONCAT(P.Nombre SEPARATOR ', ') AS ProyectosTrabajados
FROM Empleados E
JOIN EmpleadosProyectos EP ON E.ID = EP.ID_Empleado
JOIN Proyectos P ON E.ID = EP.ID_Empleado AND E.ID = P.ID_Lider
GROUP BY E.ID, E.Nombre, EP.CantidadProyectos;
