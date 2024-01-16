//
// Habilidades
//

-- Modificación de la estructura
CREATE TABLE Habilidades (
    ID_Habilidad INT PRIMARY KEY,
    Descripcion VARCHAR(50)
);

CREATE TABLE EmpleadoHabilidades (
    ID_Empleado INT,
    ID_Habilidad INT,
    FOREIGN KEY (ID_Empleado) REFERENCES Empleados(ID),
    FOREIGN KEY (ID_Habilidad) REFERENCES Habilidades(ID_Habilidad)
);
