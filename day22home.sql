-- ex6

SELECT * FROM movies
INNER JOIN boxoffice
ON movies.id = boxoffice.movie_id;

SELECT * FROM movies
INNER JOIN boxoffice
ON movies.id = boxoffice.movie_id
WHERE international_sales > domestic_sales;

SELECT * FROM movies
INNER JOIN boxoffice
ON movies.id = boxoffice.movie_id
ORDER BY rating DESC;


-- ex7
SELECT DISTINCT Building_name FROM Buildings
LEFT JOIN Employees
ON Buildings.Building_name = Employees.Building
WHERE Role NOT LIKE 'NULL';

SELECT DISTINCT Building_name, Capacity FROM Buildings;

-- SELECT Building_name, DISTINCT Role FROM Buildings
-- FULL JOIN employees
-- ON buildings.building_name = employees.building;
-- -- forgot full join doesn't work here..
-- SELECT DISTINCT Building, Employees.Role FROM Buildings
-- LEFT JOIN Employees
-- ON Buildings.Building_name = Employees.Building
-- WHERE Role LIKE '%' OR IS NULL;
-- -- incomplete - not sure how to include empty buildings

-- ex8
SELECT Name, Role FROM Employees
WHERE Building IS NULL;

SELECT DISTINCT Building_name FROM Buildings
LEFT JOIN Employees
ON Buildings.Building_name = Employees.Building
WHERE Name IS NULL;

-- ex9
SELECT Title, (Domestic_sales + International_sales) / 1000000 AS Combined_sales
FROM movies
JOIN Boxoffice
ON Movies.Id = Boxoffice.Movie_id;

SELECT Title, Rating * 10 AS Rating_perc
FROM Movies
JOIN Boxoffice
ON movies.Id = Boxoffice.Movie_id; 

SELECT Title, Year FROM Movies
WHERE Year % 2 = 0;