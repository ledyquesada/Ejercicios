--
-- Lider
--

--Paso 1.. Modificar la tabla proyectos 

--Paso 2... Encontrar empleados

SELECT E.ID, E.Nombre
FROM Empleados E
JOIN Proyectos P ON E.ID = P.ID_Lider
GROUP BY E.ID, E.Nombre
HAVING SUM(DATEDIFF(P.FechaFin, P.FechaInicio)) > 24;
