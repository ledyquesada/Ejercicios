-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS Biblioteca;

-- Seleccionar la base de datos
USE Biblioteca;

-- Crear la tabla Autores
CREATE TABLE IF NOT EXISTS Autores (
    IDAutor INT PRIMARY KEY,
    Nombre VARCHAR(255) NOT NULL
);

-- Crear la tabla Libros
CREATE TABLE IF NOT EXISTS Libros (
    IDLibro INT PRIMARY KEY,
    Titulo VARCHAR(255) NOT NULL,
    AutorID INT,
    Disponible BOOLEAN,
    FOREIGN KEY (AutorID) REFERENCES Autores(IDAutor)
);

-- Crear la tabla Usuarios
CREATE TABLE IF NOT EXISTS Usuarios (
    IDUsuario INT PRIMARY KEY,
    Nombre VARCHAR(255) NOT NULL
);

-- Crear la tabla Prestamos
CREATE TABLE IF NOT EXISTS Prestamos (
    IDPrestamo INT PRIMARY KEY,
    UsuarioID INT,
    LibroID INT,
    FechaPrestamo DATE,
    FechaDevolucion DATE,
    FOREIGN KEY (UsuarioID) REFERENCES Usuarios(IDUsuario),
    FOREIGN KEY (LibroID) REFERENCES Libros(IDLibro)
);


--Poblar base de datos
-- Insertar autores
INSERT INTO Autores (IDAutor, Nombre) VALUES (1, 'Autor1');
INSERT INTO Autores (IDAutor, Nombre) VALUES (2, 'Autor2');

-- Insertar libros
INSERT INTO Libros (IDLibro, Titulo, AutorID, Disponible) VALUES (1, 'Libro1', 1, 1);
INSERT INTO Libros (IDLibro, Titulo, AutorID, Disponible) VALUES (2, 'Libro2', 1, 1);
INSERT INTO Libros (IDLibro, Titulo, AutorID, Disponible) VALUES (3, 'Libro3', 2, 1);

-- Insertar usuarios
INSERT INTO Usuarios (IDUsuario, Nombre) VALUES (1, 'Usuario1');
INSERT INTO Usuarios (IDUsuario, Nombre) VALUES (2, 'Usuario2');

-- Insertar préstamos
INSERT INTO Prestamos (IDPrestamo, UsuarioID, LibroID, FechaPrestamo, FechaDevolucion) VALUES (1, 1, 1, '2022-01-01', '2022-01-10');
INSERT INTO Prestamos (IDPrestamo, UsuarioID, LibroID, FechaPrestamo, FechaDevolucion) VALUES (2, 1, 2, '2022-02-01', NULL);
INSERT INTO Prestamos (IDPrestamo, UsuarioID, LibroID, FechaPrestamo, FechaDevolucion) VALUES (3, 2, 3, '2022-03-01', NULL);

--CONSULTA SQL
SELECT
    L.Titulo,
    A.Nombre AS Autor,
    (
        SELECT COUNT(DISTINCT P1.UsuarioID)
        FROM Prestamos P1
        WHERE P1.LibroID = L.IDLibro
    ) AS TotalUsuariosDiferentes
FROM
    Libros AS L
JOIN
    Autores A ON L.AutorID = A.IDAutor
WHERE
    EXISTS (
        SELECT 1
        FROM Prestamos P2
        WHERE P2.LibroID = L.IDLibro
    )
    AND A.IDAutor IN (
        SELECT A2.IDAutor
        FROM Autores A2
        JOIN Libros L2 ON A2.IDAutor = L2.AutorID
        GROUP BY A2.IDAutor
        HAVING COUNT(L2.IDLibro) > 1
    );
