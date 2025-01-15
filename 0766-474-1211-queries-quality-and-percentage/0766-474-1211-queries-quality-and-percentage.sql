# Write your MySQL query statement below
SELECT 
    q1.query_name, 
    ROUND(AVG(q1.rating/q1.position), 2) AS quality,
    ROUND((SELECT COUNT(*)
            FROM Queries q2
            WHERE q2.query_name = q1.query_name AND q2.rating < 3)
     / (SELECT COUNT(*)
        FROM Queries q2
            WHERE q2.query_name = q1.query_name)
      * 100
    , 2)    AS poor_query_percentage
FROM
    Queries q1
GROUP BY q1.query_name;