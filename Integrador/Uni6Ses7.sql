-- EJERCICIO 1

BEGIN;

INSERT INTO Cursos (id_curso, nombre)
VALUES (10, 'Análisis Avanzado de Datos');

INSERT INTO Inscripciones (id_usuario, id_curso, fecha_inscripcion)
VALUES 
(1, 10, '2024-04-01'),
(2, 10, '2024-04-01'),
(3, 10, '2024-04-01');

COMMIT;


--  EJERCICIO 2

BEGIN;

INSERT INTO Inscripciones (id_usuario, id_curso, fecha_inscripcion)
VALUES (999, 1, '2024-04-01');  -- Este usuario no existe

-- Si falla, se debe hacer:
ROLLBACK;



-- ejercicio 3

CREATE TABLE Log_Inscripciones (
    id_log INTEGER PRIMARY KEY AUTOINCREMENT,
    id_usuario INT,
    id_curso INT,
    fecha_registro TEXT
);

CREATE TRIGGER tr_log_inscripcion
AFTER INSERT ON Inscripciones
BEGIN
    INSERT INTO Log_Inscripciones (id_usuario, id_curso, fecha_registro)
    VALUES (NEW.id_usuario, NEW.id_curso, datetime('now'));
END;


-- Ejercicio 4

CREATE TRIGGER tr_evitar_inscripcion_duplicada
BEFORE INSERT ON Inscripciones
WHEN EXISTS (
    SELECT 1 FROM Inscripciones
    WHERE id_usuario = NEW.id_usuario AND id_curso = NEW.id_curso
)
BEGIN
    SELECT RAISE(ABORT, 'El usuario ya está inscrito en este curso');
END;




