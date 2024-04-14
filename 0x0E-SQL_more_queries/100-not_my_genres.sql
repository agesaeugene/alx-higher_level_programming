-- utilizes the database hbtn_0d_tvshows to display all genres that aren't associated with the program. Dexter
-- a database is used to link all rows not linked to one row.
-- tv_genre.name should display each record.
SELECT name
FROM tv_genres
WHERE name NOT IN
(SELECT name
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
LEFT JOIN tv_show ON tv_show_genres.show_id = tv_show.id
WHERE tv_shows.title = 'Dexter')
GROUP BY name
ORDER BY name ASC
