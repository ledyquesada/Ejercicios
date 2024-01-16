//
// Tabla poyectos
//

//Creacion 
CREATE TABLE Proyectos (
    ID INT PRIMARY KEY,
    Nombre VARCHAR(50),
    FechaInicio DATE
);

//Inseerción

INSERT INTO Proyectos (ID, Nombre, FechaInicio) VALUES
(1, 'Proyecto Web', '2019-01-15'),
(2, 'Proyecto Móvil', '2022-02-01');
(3, 'Proyecto SQL', '2023-05-11');
(4, 'Proyecto Python', '2024-01-01');
(5, 'Proyecto Angular', '2022-09-01');
