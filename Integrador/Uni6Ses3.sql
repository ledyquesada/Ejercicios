//Ejercicio 1

SELECT c.nombre AS curso, COUNT(i.id_usuario) AS total_inscritos
FROM Inscripciones i
JOIN Cursos c ON i.id_curso = c.id_curso
GROUP BY c.nombre
ORDER BY total_inscritos DESC;


//Ejercicio 2
SELECT c.nombre AS curso, COUNT(i.id_usuario) AS inscritos
FROM Inscripciones i
JOIN Cursos c ON i.id_curso = c.id_curso
GROUP BY c.nombre
HAVING COUNT(i.id_usuario) > 2;


//Ejercicio 3

SELECT u.nombre, COUNT(i.id_curso) AS total_cursos
FROM Usuarios u
JOIN Inscripciones i ON u.id_usuario = i.id_usuario
GROUP BY u.nombre
HAVING COUNT(i.id_curso) > (
    SELECT AVG(cursos_por_usuario)
    FROM (
        SELECT COUNT(*) AS cursos_por_usuario
        FROM Inscripciones
        GROUP BY id_usuario
    ) AS sub;
);

//Ejercicio 4

SELECT 
    strftime('%Y-%m', fecha_inscripcion) AS mes,
    COUNT(*) AS total_inscripciones
FROM Inscripciones
GROUP BY mes
ORDER BY mes DESC;




