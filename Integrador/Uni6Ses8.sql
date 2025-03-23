--Ejercicio 1

CREATE TABLE Clientes (
    id_cliente INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    email TEXT UNIQUE
);

CREATE TABLE Productos (
    id_producto INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    precio REAL NOT NULL
);

CREATE TABLE Pedidos (
    id_pedido INTEGER PRIMARY KEY,
    id_cliente INTEGER,
    fecha TEXT,
    FOREIGN KEY (id_cliente) REFERENCES Clientes(id_cliente)
);

CREATE TABLE DetallePedidos (
    id_pedido INTEGER,
    id_producto INTEGER,
    cantidad INTEGER,
    PRIMARY KEY (id_pedido, id_producto),
    FOREIGN KEY (id_pedido) REFERENCES Pedidos(id_pedido),
    FOREIGN KEY (id_producto) REFERENCES Productos(id_producto)
);

--Ejercicio 2

-- Clientes
INSERT INTO Clientes (id_cliente, nombre, email) VALUES
(1, 'Laura Vélez', 'laura@example.com'),
(2, 'Juan Orozco', 'juan@example.com');

-- Productos
INSERT INTO Productos (id_producto, nombre, precio) VALUES
(101, 'Laptop', 2500),
(102, 'Mouse', 80),
(103, 'Audífonos', 150);

-- Pedidos
INSERT INTO Pedidos (id_pedido, id_cliente, fecha) VALUES
(1001, 1, '2024-04-01'),
(1002, 2, '2024-04-02');

-- Detalle de pedidos
INSERT INTO DetallePedidos (id_pedido, id_producto, cantidad) VALUES
(1001, 101, 1),
(1001, 102, 2),
(1002, 102, 1),
(1002, 103, 1);

--Ejercicio 3

SELECT 
  c.nombre AS cliente,
  p.nombre AS producto,
  dp.cantidad,
  (dp.cantidad * p.precio) AS total_gastado
FROM DetallePedidos dp
JOIN Pedidos pe ON dp.id_pedido = pe.id_pedido
JOIN Clientes c ON pe.id_cliente = c.id_cliente
JOIN Productos p ON dp.id_producto = p.id_producto;


--Ejercicio 4

CREATE VIEW Vista_GastoClientes AS
SELECT 
  c.nombre,
  SUM(dp.cantidad * p.precio) AS total_gastado
FROM Clientes c
JOIN Pedidos pe ON c.id_cliente = pe.id_cliente
JOIN DetallePedidos dp ON pe.id_pedido = dp.id_pedido
JOIN Productos p ON dp.id_producto = p.id_producto
GROUP BY c.id_cliente;


