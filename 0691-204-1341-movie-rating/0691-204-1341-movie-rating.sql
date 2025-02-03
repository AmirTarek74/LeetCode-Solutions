# Write your MySQL query statement below
WITH MostRated AS
(
    SELECT
        user_id,
        COUNT(user_id) AS Rated
    FROM
        MovieRating 
    GROUP BY
        user_id 
),
Names AS 
(
    SELECT u.name, MostRated.Rated  FROM MostRated
    JOIN Users u ON u.user_id = MostRated.user_id
    WHERE MostRated.Rated = (SELECT MAX(MostRated.Rated) FROM MostRated)
),
TopUser AS
(
    SELECT name FROM Names
    WHERE name =(SELECT min(name) FROM Names)  
),
TopMovies AS(
    SELECT movie_id, AVG(rating) as AVG_1 FROM MovieRating 
    WHERE MONTH(created_at ) = 2 AND YEAR(created_at )=2020
    GROUP BY movie_id

),
MoviesName AS
(
    SELECT m.title, AVG_1 FROM TopMovies 
    JOIN Movies m ON m.movie_id = TopMovies.movie_id
    WHERE AVG_1 = (SELECT MAX(AVG_1) FROM TopMovies)
),
TopMovie AS
(
    SELECT title FROM MoviesName
    WHERE title = (SELECT MIN(title) FROM MoviesName)
)
SELECT name AS results FROM TopUser 
UNION ALL
SELECT title FROM TopMovie