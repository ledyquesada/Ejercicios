CREATE TABLE Clientes (
    IDCliente INT PRIMARY KEY,
    Nombre VARCHAR(50),
    Ciudad VARCHAR(30)
);

CREATE TABLE Productos (
    IDProducto INT PRIMARY KEY,
    NombreProducto VARCHAR(50),
    Precio DECIMAL(10, 2)
);

CREATE TABLE Ventas (
    IDVenta INT PRIMARY KEY,
    IDCliente INT,
    IDProducto INT,
    Cantidad INT,
    FechaVenta DATE,
    FOREIGN KEY (IDCliente) REFERENCES Clientes(IDCliente),
    FOREIGN KEY (IDProducto) REFERENCES Productos(IDProducto)
);

-- Población de datos de ejemplo
INSERT INTO Clientes (IDCliente, Nombre, Ciudad) VALUES
(1, 'Juan Perez', 'Bogotá'),
(2, 'Maria Rodriguez', 'Medellín'),
(3, 'Carlos Gómez', 'Cali');

INSERT INTO Productos (IDProducto, NombreProducto, Precio) VALUES
(101, 'Televisor LED 50 pulgadas', 1500.00),
(102, 'Smartphone Android', 500.00),
(103, 'Laptop Core i5', 1200.00);

INSERT INTO Ventas (IDVenta, IDCliente, IDProducto, Cantidad, FechaVenta) VALUES
(1001, 1, 101, 2, '2022-01-10'),
(1002, 2, 102, 1, '2022-01-11'),
(1003, 1, 103, 1, '2022-01-12'),
(1004, 3, 101, 3, '2022-01-12');

-- 1. Clientes que más Compraron por Producto
WITH ClientesPorProducto AS (
    SELECT
        V.IDProducto,
        V.IDCliente,
        C.Nombre AS NombreCliente,
        P.NombreProducto,
        V.Cantidad,
        ROW_NUMBER() OVER (PARTITION BY V.IDProducto ORDER BY V.Cantidad DESC) AS Rn
    FROM Ventas V
    JOIN Productos P ON V.IDProducto = P.IDProducto
    JOIN Clientes C ON V.IDCliente = C.IDCliente
)
SELECT
    NombreProducto,
    NombreCliente,
    Cantidad
FROM ClientesPorProducto
WHERE Rn = 1;

-- 2. Productos más Vendidos por Ciudad
SELECT
    P.NombreProducto,
    C.Ciudad,
    SUM(V.Cantidad) AS CantidadTotal,
    SUM(V.Cantidad * P.Precio) AS PrecioTotal
FROM Ventas V
JOIN Productos P ON V.IDProducto = P.IDProducto
JOIN Clientes C ON V.IDCliente = C.IDCliente
GROUP BY P.NombreProducto, C.Ciudad
ORDER BY CantidadTotal DESC;

-- 3. Días de Mayor Actividad Comercial
SELECT
    FechaVenta,
    COUNT(*) AS VentasRealizadas
FROM Ventas
GROUP BY FechaVenta
ORDER BY VentasRealizadas DESC;
