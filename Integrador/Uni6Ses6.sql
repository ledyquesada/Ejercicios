//Ejercicio 1

CREATE VIEW Vista_Inscripciones_Detalle AS
SELECT 
    u.nombre AS nombre_usuario,
    c.nombre AS nombre_curso,
    i.fecha_inscripcion
FROM Inscripciones i
JOIN Usuarios u ON i.id_usuario = u.id_usuario
JOIN Cursos c ON i.id_curso = c.id_curso;


//Ejercicio 2

CREATE VIEW Vista_Resumen_Usuarios AS
SELECT 
    u.nombre,
    COUNT(i.id_curso) AS total_cursos
FROM Usuarios u
LEFT JOIN Inscripciones i ON u.id_usuario = i.id_usuario
GROUP BY u.id_usuario;


//Ejercicio 3

CREATE INDEX idx_usuarios_email ON Usuarios(email);



