# Write your MySQL query statement below
SELECT
    CASE
        WHEN COUNT(*)=0 THEN NULL
        ELSE salary
    END AS SecondHighestSalary
FROM
    (
        SELECT *,
        ROW_NUMBER() OVER(ORDER BY salary DESC) as r
        FROM
        (
            SELECT DISTINCT salary FROM Employee) as A 
        ) as B
    WHERE r = 2
    