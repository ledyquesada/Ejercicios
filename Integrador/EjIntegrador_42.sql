//
//Aumento salario departamento
//

DELIMITER //
CREATE PROCEDURE AumentarSalariosEnDepartamento(IN dept_id INT, IN porcentaje_aumento DECIMAL(5,2))
BEGIN
    UPDATE Empleados
    SET Salario = Salario * (1 + porcentaje_aumento / 100)
    WHERE ID_Departamento = dept_id;
END //
DELIMITER ;
