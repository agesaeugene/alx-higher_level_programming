-- use the hbtn_0d_tvshows database to list every program genre. Dexter is
-- a database is used to list all rows in a table corresponding to all rows in another.
-- each record should display all tv_genre.name
SELECT name
FROM tv_genres
INNER JOIN tv_show_genres m ON tv_genres.id = m.genre_id
INNER JOIN tv_shows s ON m.show_id = s.id
WHERE s.title = 'Dexter'
ORDER BY tv_genres.name ASC;
