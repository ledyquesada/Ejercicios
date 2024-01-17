--
-- Top 10%
--

WITH TopSalarios AS (
    SELECT ID_Departamento, Salario,
           ROW_NUMBER() OVER (PARTITION BY ID_Departamento ORDER BY Salario DESC) AS Rnk
    FROM Empleados
)
SELECT ID_Departamento, Salario
FROM TopSalarios
WHERE Rnk <= 0.1 * COUNT(*) OVER (PARTITION BY ID_Departamento);
