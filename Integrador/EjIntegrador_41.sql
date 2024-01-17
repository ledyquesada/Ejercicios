//
// Departamento con salario alto
//

-- Paso 1: Crear la tabla "Departamentos"
CREATE TABLE Departamentos (
    ID INT PRIMARY KEY,
    Nombre VARCHAR(50)
);

-- Paso 2: Modificar la tabla "Empleados" para agregar la columna "ID_Departamento"
ALTER TABLE Empleados
ADD COLUMN ID_Departamento INT,
ADD FOREIGN KEY (ID_Departamento) REFERENCES Departamentos(ID);


-- Paso 3: Insertar registros en "Departamentos" y "Empleados"
INSERT INTO Departamentos (ID, Nombre) VALUES
(1, 'Ventas'),
(2, 'Desarrollo'),
(3, 'Finanzas');

-- Asignar departamentos a empleados existentes
UPDATE Empleados
SET ID_Departamento = CASE
    WHEN ID = 1 THEN 1  -- Asignar departamento a empleado con ID 1
    WHEN ID = 2 THEN 2  -- Asignar departamento a empleado con ID 2
    WHEN ID = 3 THEN 1  -- Asignar departamento a empleado con ID 3
    WHEN ID = 4 THEN 3  -- Asignar departamento a empleado con ID 4
    -- Añadir más casos según sea necesario
    ELSE NULL
END;

-- Paso 4: Calcular el total pagado en salarios por cada departamento
SELECT D.Nombre AS Departamento, COALESCE(SUM(E.Salario), 0) AS TotalSalarios
FROM Departamentos D
LEFT JOIN Empleados E ON D.ID = E.ID_Departamento
GROUP BY D.Nombre;
