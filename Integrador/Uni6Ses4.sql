//Ejercicio 1

SELECT u.nombre, COUNT(i.id_curso) AS total_inscripciones
FROM Usuarios u
JOIN Inscripciones i ON u.id_usuario = i.id_usuario
GROUP BY u.id_usuario
HAVING COUNT(i.id_curso) > (
    SELECT AVG(inscripciones_por_usuario)
    FROM (
        SELECT COUNT(*) AS inscripciones_por_usuario
        FROM Inscripciones
        GROUP BY id_usuario
    )
);

//Ejercicio 2

SELECT DISTINCT u.nombre
FROM Usuarios u
WHERE NOT EXISTS (
    SELECT id_curso
    FROM Inscripciones
    WHERE id_usuario = 1
    EXCEPT
    SELECT id_curso
    FROM Inscripciones i
    WHERE i.id_usuario = u.id_usuario
);


//Ejercicio 3

SELECT u.nombre,
  CASE
    WHEN COUNT(i.id_curso) > 2 THEN 'Alto'
    WHEN COUNT(i.id_curso) = 2 THEN 'Medio'
    WHEN COUNT(i.id_curso) = 1 THEN 'Bajo'
    ELSE 'Sin cursos'
  END AS nivel_inscripcion
FROM Usuarios u
LEFT JOIN Inscripciones i ON u.id_usuario = i.id_usuario
GROUP BY u.id_usuario;


//Ejercicio 4

SELECT c.nombre AS curso,
  COUNT(i.id_usuario) AS inscritos,
  CASE
    WHEN COUNT(i.id_usuario) > 3 THEN 'Popular'
    WHEN COUNT(i.id_usuario) BETWEEN 2 AND 3 THEN 'Regular'
    ELSE 'Poco demandado'
  END AS clasificacion
FROM Cursos c
LEFT JOIN Inscripciones i ON c.id_curso = i.id_curso
GROUP BY c.id_curso;



