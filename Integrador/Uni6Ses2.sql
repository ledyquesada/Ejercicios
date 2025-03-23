//Ejercicio 1
-- Productos
INSERT INTO Productos (id_producto, nombre, categoria)
VALUES (1, 'Laptop', 'Tecnología'),
       (2, 'Café', 'Alimentos');

-- Clientes
INSERT INTO Clientes (id_cliente, nombre, ciudad)
VALUES (101, 'Lucía Rojas', 'Bogotá'),
       (102, 'Marco Díaz', 'Tunja');

-- Ventas
INSERT INTO Ventas (id_venta, id_producto, id_cliente, cantidad, fecha_venta)
VALUES 
(1001, 1, 101, 1, '2024-01-15'),
(1002, 2, 102, 5, '2024-01-20'),
(1003, 2, 101, 3, '2024-01-25');

//Ejercicio2

SELECT c.nombre AS cliente, p.nombre AS producto, v.cantidad
FROM Ventas v
JOIN Clientes c ON v.id_cliente = c.id_cliente
JOIN Productos p ON v.id_producto = p.id_producto
WHERE p.categoria = 'Alimentos'
ORDER BY v.cantidad DESC;

//Ejercicio 3

SELECT p.nombre AS producto, p.categoria, SUM(v.cantidad) AS total_vendido
FROM Ventas v
JOIN Productos p ON v.id_producto = p.id_producto
GROUP BY p.nombre, p.categoria
ORDER BY total_vendido DESC;


//Ejercicio 4

SELECT c.nombre, SUM(v.cantidad) AS total_cliente
FROM Clientes c
JOIN Ventas v ON c.id_cliente = v.id_cliente
GROUP BY c.nombre
HAVING SUM(v.cantidad) > (
    SELECT AVG(cantidad_total)
    FROM (
        SELECT SUM(v2.cantidad) AS cantidad_total
        FROM Ventas v2
        GROUP BY v2.id_cliente
    ) AS promedio_clientes
);




