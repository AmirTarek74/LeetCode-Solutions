# Write your MySQL query statement below
DELETE FROM Person 
WHERE
    id NOT IN (SELECT min_id FROM (SELECT min(id) AS min_id FROM Person  GROUP BY email) as a)