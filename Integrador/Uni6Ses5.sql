//Ejerccio 1

SELECT 
  id_pedido,
  region,
  monto,
  ROW_NUMBER() OVER (PARTITION BY region ORDER BY fecha) AS orden_en_region
FROM Pedidos;


//Ejercicio 2

SELECT 
  id_pedido,
  region,
  monto,
  RANK() OVER (PARTITION BY region ORDER BY monto DESC) AS rank_en_region
FROM Pedidos;


//Ejercicio 3

WITH ranked_pedidos AS (
  SELECT *,
         ROW_NUMBER() OVER (PARTITION BY region ORDER BY monto DESC) AS rn
  FROM Pedidos
)
SELECT id_pedido, region, monto
FROM ranked_pedidos
WHERE rn = 1;


//Ejercicio 4

SELECT 
  id_pedido,
  monto,
  NTILE(4) OVER (ORDER BY monto DESC) AS cuartil
FROM Pedidos;


//Ejercicio 5

WITH resumen_region AS (
  SELECT region, AVG(monto) AS promedio_region
  FROM Pedidos
  GROUP BY region
)
SELECT 
  region,
  promedio_region,
  RANK() OVER (ORDER BY promedio_region DESC) AS rank_nacional
FROM resumen_region;


