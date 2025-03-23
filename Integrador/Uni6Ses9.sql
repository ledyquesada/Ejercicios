--Ejercicio 1
CREATE TABLE Estudiantes (
    id_estudiante INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    municipio TEXT,
    email TEXT UNIQUE
);

CREATE TABLE Programas (
    id_programa INTEGER PRIMARY KEY,
    nombre TEXT,
    sector TEXT
);

CREATE TABLE Clases (
    id_clase INTEGER PRIMARY KEY,
    id_programa INTEGER,
    tema TEXT,
    fecha TEXT,
    FOREIGN KEY (id_programa) REFERENCES Programas(id_programa)
);

CREATE TABLE Asistencias (
    id_estudiante INTEGER,
    id_clase INTEGER,
    asistio INTEGER, -- 1 = sí, 0 = no
    PRIMARY KEY (id_estudiante, id_clase),
    FOREIGN KEY (id_estudiante) REFERENCES Estudiantes(id_estudiante),
    FOREIGN KEY (id_clase) REFERENCES Clases(id_clase)
);


--Ejercicio 2

-- Estudiantes
INSERT INTO Estudiantes VALUES (1, 'Ana Ríos', 'Tunja', 'ana@example.com');
-- ...otros

-- Programas
INSERT INTO Programas VALUES (1, 'Formación en TIC', 'Tecnología');
-- ...otro programa

-- Clases
INSERT INTO Clases VALUES (101, 1, 'Introducción a TIC', '2024-03-01');
-- ...otras clases

-- Asistencias
INSERT INTO Asistencias VALUES (1, 101, 1);
-- ...otras asistencias


--Ejercicio 3
--pregunta a
SELECT 
  e.nombre,
  ROUND(100.0 * SUM(a.asistio) / COUNT(*), 2) AS porcentaje_asistencia
FROM Estudiantes e
JOIN Asistencias a ON e.id_estudiante = a.id_estudiante
GROUP BY e.id_estudiante;


--pregunta b
SELECT 
  p.nombre AS programa,
  ROUND(AVG(a.asistio) * 100, 2) AS tasa_asistencia
FROM Asistencias a
JOIN Clases c ON a.id_clase = c.id_clase
JOIN Programas p ON c.id_programa = p.id_programa
GROUP BY p.id_programa
ORDER BY tasa_asistencia DESC
LIMIT 1;


--pregunta c

SELECT nombre
FROM Estudiantes
WHERE id_estudiante NOT IN (
  SELECT DISTINCT id_estudiante
  FROM Asistencias
  WHERE asistio = 1
);


--pregunta d

SELECT 
  p.sector,
  COUNT(DISTINCT c.id_clase) AS total_clases
FROM Clases c
JOIN Programas p ON c.id_programa = p.id_programa
GROUP BY p.sector;


