//
// Asignaciones
//

//Creacion 

CREATE TABLE Asignaciones (
    ID_Empleado INT,
    ID_Proyecto INT,
    FOREIGN KEY (ID_Empleado) REFERENCES Empleados(ID),
    FOREIGN KEY (ID_Proyecto) REFERENCES Proyectos(ID)
);

//Asignacion de 1 empleado

INSERT INTO Asignaciones (ID_Empleado, ID_Proyecto) VALUES (1, 1);
// Repite la linea anterior 2 veces mas de acuerdo a tus empleados y tus proyectos

//Listar

SELECT E.Nombre
FROM Empleados E
JOIN Asignaciones A ON E.ID = A.ID_Empleado
JOIN Proyectos P ON A.ID_Proyecto = P.ID
WHERE P.Id = 2;
