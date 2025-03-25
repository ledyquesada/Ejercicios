--Ejercicio 1
CREATE TABLE Eventos_Plataforma (
    id_evento INTEGER PRIMARY KEY,
    id_estudiante INTEGER,
    actividad TEXT,
    fecha_evento TEXT,
    clase_id INTEGER
);


--Ejercicio 2

CREATE VIEW RegistroEventos AS
SELECT 
  id_estudiante AS case_id,
  actividad AS activity,
  fecha_evento AS timestamp
FROM Eventos_Plataforma;


--Ejercicio 3

SELECT 
  id_estudiante AS case_id,
  actividad AS activity,
  fecha_evento AS timestamp
FROM Eventos_Plataforma
WHERE actividad IS NOT NULL AND fecha_evento IS NOT NULL
ORDER BY id_estudiante, fecha_evento;
