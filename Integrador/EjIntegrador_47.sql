--
--Diferencia de salario
--

SELECT ID_Departamento
FROM (
    SELECT ID_Departamento, MAX(Salario) - MIN(Salario) AS DiferenciaSalarios
    FROM Empleados
    GROUP BY ID_Departamento
) SalariosDepartamento
WHERE DiferenciaSalarios > 30000;
