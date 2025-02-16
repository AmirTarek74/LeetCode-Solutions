# Write your MySQL query statement below
WITH grouped AS
(
    SELECT product_id,
    order_date,
    SUM(unit) as unit
    FROM
        Orders
    
    WHERE order_date like '2020-02-%'
    GROUP BY product_id
)
SELECT p.product_name     , g.unit
FROM Products p
JOIN grouped g on g.product_id = p.product_id
WHERE g.unit >= 100 