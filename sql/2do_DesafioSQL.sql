-- Tablas asociadas:
/*
tabla de Producto -> productos (product_id, product_name, product_cost, product_stock)
tabla de Clientes ->  clientes (customer_id, customer_name)
tabla de Invoice -> (invoice_id, invoice_date, invoice_product_id, invoice_mount)
*/

-- Identificar los productos mas vendidos del ultimo mes
WITH ventas_ultimo_mes AS (
    SELECT
        product_id,
        product_name,
        SUM(invoice_mount) AS total_ventas,
        COUNT(*) AS cantidad_vendida
        RANK() OVER(PARTITION BY name ORDER BY count(*) DESC) AS rank
    FROM productos
    JOIN invoice 
    ON product_id = invoice_product_id
    WHERE invoice_date >= DATEADD(MONTH, -1, GETDATE())
    GROUP BY product_id, product_name
),

--Obtener los clientes que compraron estos productos, ordenados por volumen de compra
clientes_por_volumen AS (
    SELECT
        customer_id,
        customer_name,
        product_id,
        SUM (invoice_mount) AS total_comprado
    FROM ventas_ultimo_mes
    JOIN inovice 
    ON product_id = invoice_product_id
    JOIN clientes 
    ON invoice_costumer_id = customer_id
    GROUP BY customer_id, customer_name, product_id
    ORDER BY total_comprado DESC
)

-- Calcular el monto total de ventas por cliente
ventas_por_cliente AS (
    SELECT
        customer_id,
        customer_name,
        SUM(total_comprado) AS total_ventas,
        RANK() OVER(ORDER BY total_ventas DESC) AS rank
    FROM clientes_por_volumen
    GROUP BY customer_id, customer_name
)

--Resultados
SELECT
    customer_name,
    product_name,
    total_vetas,
    rank
FROM clientes_por_volumen
JOIN productos 
ON productos.product_id = ventas_ultimo_mes.product_id
JOIN ventas_por_cliente 
ON clientes_por_volumen.customer_id = ventas_por_cliente.customer_id
ORDER BY rank, product_name;
