# Write your MySQL query statement below
WITH cnts AS 
(
    SELECT
        num,
        COUNT(num) AS cnt
    FROM
        MyNumbers
    GROUP BY
        num
    HAVING 
        cnt = 1
)
SELECT
    max(num) as num
FROM
    cnts;