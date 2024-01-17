--
-- Años de experiencia
--

SELECT ID_Proyecto
FROM (
    SELECT EP.ID_Proyecto, COUNT(*) AS CantidadEmpleados
    FROM EmpleadosProyectos EP
    JOIN Empleados E ON EP.ID_Empleado = E.ID
    WHERE E.Experiencia > 5
    GROUP BY EP.ID_Proyecto
) ProyectosExperiencia
WHERE CantidadEmpleados = (
    SELECT COUNT(*) FROM EmpleadosProyectos WHERE ID_Proyecto = ProyectosExperiencia.ID_Proyecto
);
