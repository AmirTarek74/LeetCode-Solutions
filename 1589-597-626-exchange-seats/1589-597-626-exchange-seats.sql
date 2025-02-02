select
CASE
    WHEN id = (SELECT MAX(id) FROM Seat) AND id%2 = 1 then id
    WHEN id % 2 = 1 then id + 1 else id - 1  
     
    END AS id,
    student
FROM
    Seat
ORDER BY id;