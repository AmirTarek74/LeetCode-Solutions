# Write your MySQL query statement below
WITH CTE AS (
    SELECT *, SUM(weight) OVER (ORDER BY turn) AS rolling_weight
    FROM
        Queue
)
SELECT person_name from CTE WHERE rolling_weight <= 1000
ORDER BY rolling_weight DESC 
LIMIT 1;