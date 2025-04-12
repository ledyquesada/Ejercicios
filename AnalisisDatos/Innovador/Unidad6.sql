--Ejercicio 1

SELECT nombre, id
FROM Estudiantes
WHERE id IN (
    SELECT estudiante_id
    FROM Inscripciones i1
    WHERE calificacion > (
        SELECT AVG(calificacion)
        FROM Inscripciones i2
        WHERE i1.curso_id = i2.curso_id
    )
);

--Ejercicio 2
SELECT
    estudiante_id,
    monto,
    SUM(monto) OVER (PARTITION BY estudiante_id) AS total_por_estudiante,
    ROUND(100.0 * monto / SUM(monto) OVER (PARTITION BY estudiante_id), 2) AS porcentaje
FROM Pagos;


--Ejercicio 3

WITH CursoOrdenado AS (
    SELECT *, ROW_NUMBER() OVER (PARTITION BY categoria ORDER BY duracion DESC) AS rk
    FROM Cursos
)
SELECT * FROM CursoOrdenado WHERE rk <= 2;

--Ejercicio 4

SELECT e.ciudad, COUNT(DISTINCT e.id) AS total_estudiantes
FROM Estudiantes e
JOIN Inscripciones i ON e.id = i.estudiante_id
JOIN Cursos c ON i.curso_id = c.id
WHERE c.duracion > 40
GROUP BY e.ciudad;

--SESION 2

--EJERCICIO 1

CREATE INDEX idx_estudiantes_ciudad ON Estudiantes (ciudad);

-- Consulta a optimizar
SELECT * FROM Estudiantes WHERE ciudad = 'Bogotá';


--EJERCICIO 2

CREATE INDEX idx_inscripciones_estudiante ON Inscripciones (estudiante_id);
CREATE INDEX idx_pagos_estudiante ON Pagos (estudiante_id);

-- Consulta a optimizar
SELECT i.*, p.*
FROM Inscripciones i
JOIN Pagos p ON i.estudiante_id = p.estudiante_id;


--EJERCICIO 3

-- En motores como PostgreSQL
EXPLAIN ANALYZE
SELECT * FROM Estudiantes WHERE ciudad = 'Tunja';


--EJERCICIO  4

-- Verificación previa
SELECT nombre, COUNT(*) FROM Cursos GROUP BY nombre HAVING COUNT(*) > 1;

-- Intento de índice único
CREATE UNIQUE INDEX idx_curso_nombre ON Cursos (nombre);

--SESION 3
--EJERCICIO 1

SELECT ciudad,
    AVG(CASE WHEN c.categoria = 'Ciencia' THEN i.calificacion END) AS Ciencia,
    AVG(CASE WHEN c.categoria = 'Tecnología' THEN i.calificacion END) AS Tecnología,
    AVG(CASE WHEN c.categoria = 'Negocios' THEN i.calificacion END) AS Negocios
FROM Estudiantes e
JOIN Inscripciones i ON e.id = i.estudiante_id
JOIN Cursos c ON i.curso_id = c.id
GROUP BY ciudad;


--EJERCICIO 2

-- Crear tabla temporal o vista si es necesario
SELECT estudiante_id, metodo_pago, monto
FROM Pagos;

--EJERCICIO 3

SELECT ciudad,
    SUM(CASE WHEN MONTH(p.fecha_pago) = 1 THEN p.monto ELSE 0 END) AS Enero,
    SUM(CASE WHEN MONTH(p.fecha_pago) = 2 THEN p.monto ELSE 0 END) AS Febrero,
    SUM(CASE WHEN MONTH(p.fecha_pago) = 3 THEN p.monto ELSE 0 END) AS Marzo
FROM Estudiantes e
JOIN Pagos p ON e.id = p.estudiante_id
GROUP BY ciudad;


--EJERCICIO 4

-- Supongamos una tabla con columnas: estudiante_id, enero, febrero, marzo
SELECT estudiante_id, Mes, Monto
FROM (
    SELECT estudiante_id, enero, febrero, marzo
    FROM PagosMensuales
) p
UNPIVOT (
    Monto FOR Mes IN (enero, febrero, marzo)
) AS unpivoted;







