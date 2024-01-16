//
// Gestor de proyectos
//

CREATE DATABASE GestorProyectos;

USE GestorProyectos;

CREATE TABLE Empleados (
    ID INT PRIMARY KEY,
    Nombre VARCHAR(50),
    Cargo VARCHAR(50),
    Salario DECIMAL(10, 2)
);
