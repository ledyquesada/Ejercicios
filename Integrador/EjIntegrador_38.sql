//
// Funcion salario
//

DELIMITER //
CREATE FUNCTION SalarioPromedio() RETURNS DECIMAL(10, 2)
BEGIN
    DECLARE promedio DECIMAL(10, 2);
    SELECT AVG(Salario) INTO promedio FROM Empleados;
    RETURN promedio;
END //
DELIMITER ;
