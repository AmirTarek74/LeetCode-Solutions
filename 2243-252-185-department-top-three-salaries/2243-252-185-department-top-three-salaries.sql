WITH emp_deprt AS 
(
    SELECT
        d.id,
        d.name AS Department,
        e.name AS Employee,
        e.salary AS Salary,
        DENSE_RANK()OVER(PARTITION BY d.id ORDER BY e.salary  DESC) AS rnk
    FROM
        Department d
    JOIN Employee e
    ON e.departmentId = d.id
)
SELECT Department, Employee, Salary FROM emp_deprt
WHERE rnk <= 3