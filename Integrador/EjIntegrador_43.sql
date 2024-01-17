//
//Bonificación
//

DELIMITER //
CREATE PROCEDURE CalcularBonificacion(IN emp_id INT)
BEGIN
    DECLARE bonificacion DECIMAL(10, 2);
    SELECT (Salario * 0.05) + (COUNT(H.ID_Habilidad) * 0.02)
    INTO bonificacion
    FROM Empleados E
    LEFT JOIN EmpleadoHabilidades EH ON E.ID = EH.ID_Empleado
    LEFT JOIN Habilidades H ON EH.ID_Habilidad = H.ID_Habilidad
    WHERE E.ID = emp_id;

    SELECT bonificacion AS Bonificacion;
END //
DELIMITER ;
