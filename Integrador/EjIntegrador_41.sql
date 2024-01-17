//
// Departamento con salario alto
//

SELECT D.Nombre AS Departamento
FROM Empleados E
JOIN Departamentos D ON E.ID_Departamento = D.ID
GROUP BY D.Nombre
HAVING AVG(E.Salario) > (SELECT SalarioPromedio() FROM DUAL);
