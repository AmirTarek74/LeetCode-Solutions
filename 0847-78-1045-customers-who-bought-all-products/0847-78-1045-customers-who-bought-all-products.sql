# Write your MySQL query statement below
WITH unique_key AS
(
    SELECT
        customer_id,
        COUNT(DISTINCT product_key) AS cnt
    FROM
        Customer 
    GROUP BY
        customer_id
)
SELECT 
    customer_id
FROM 
    unique_key
WHERE cnt = (
    SELECT 
        COUNT(*)
    FROM
        Product 
)