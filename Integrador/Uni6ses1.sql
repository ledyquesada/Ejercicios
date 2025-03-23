//Usuarios ejercicio 1
CREATE TABLE Usuarios (
    id_usuario INT PRIMARY KEY,
    nombre VARCHAR(50),
    email VARCHAR(100)
);

// ejercicio 2
CREATE TABLE Pedidos (
    id_pedido INT PRIMARY KEY,
    fecha DATE,
    id_usuario INT,
    FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario)
);

//ejercicio 3

ALTER TABLE Usuarios
ADD CONSTRAINT unique_email UNIQUE (email);

//ejercicio 4

CREATE TABLE Cursos (
    id_curso INT PRIMARY KEY,
    nombre VARCHAR(100)
);

CREATE TABLE Inscripciones (
    id_usuario INT,
    id_curso INT,
    fecha_inscripcion DATE,
    PRIMARY KEY (id_usuario, id_curso),
    FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario),
    FOREIGN KEY (id_curso) REFERENCES Cursos(id_curso)
);

