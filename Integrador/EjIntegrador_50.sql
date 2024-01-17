--
-- Salario maximo otros departamentos
--

WITH SalariosPromedio AS (
    SELECT ID_Departamento, AVG(Salario) AS SalarioPromedio
    FROM Empleados
    GROUP BY ID_Departamento
)
SELECT SP1.ID_Departamento
FROM SalariosPromedio SP1
WHERE SP1.SalarioPromedio > ALL (
    SELECT MAX(Salario)
    FROM SalariosPromedio SP2
    WHERE SP2.ID_Departamento <> SP1.ID_Departamento
);
