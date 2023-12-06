SELECT DISTINCT name
FROM people
JOIN movies ON people.id = movies.id
JOIN directors ON directors.movie_id = movies.id
JOIN ratings ON ratings.movie_id = movies.id
WHERE ratings.rating >= 9.0;

