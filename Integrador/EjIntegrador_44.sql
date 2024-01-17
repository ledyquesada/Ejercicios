//
--trigger
//

DELIMITER //
CREATE TRIGGER AsignarHabilidades
AFTER INSERT ON Empleados
FOR EACH ROW
BEGIN
    INSERT INTO EmpleadoHabilidades (ID_Empleado, ID_Habilidad)
    SELECT NEW.ID, ID_Habilidad FROM Habilidades;
END //
DELIMITER ;
