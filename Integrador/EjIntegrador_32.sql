//
//Inserción y aumento
//

  //Inserción
INSERT INTO Empleados (ID, Nombre, Cargo, Salario) VALUES
(1, 'Juan Pérez', 'Desarrollador', 50000.00),
(2, 'María González', 'Diseñador', 45000.00),
(3, 'Carlos Rodríguez', 'Gerente de Proyecto', 70000.00);

//Aumento

UPDATE Empleados SET Salario = Salario * 1.1;
