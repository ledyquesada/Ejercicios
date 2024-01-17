--
-- Compañeros de trabajo
--

WITH CompanerosSalarios AS (
    SELECT E1.ID AS IDEmpleado, E1.ID_Departamento,
           COUNT(DISTINCT E2.ID) AS CantidadCompaneros
    FROM Empleados E1
    JOIN Empleados E2 ON E1.ID_Departamento = E2.ID_Departamento
                    AND E1.ID <> E2.ID
                    AND E2.Salario BETWEEN 60000 AND 80000
    GROUP BY E1.ID, E1.ID_Departamento
)
SELECT E.*
FROM Empleados E
JOIN CompanerosSalarios CS ON E.ID = CS.IDEmpleado
WHERE CS.CantidadCompaneros >= 3;
