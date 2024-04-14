-- all genres from hbtn_0d_tvshows are listed and number of shows linked to each are displayed
-- all rows of a database meeting a condition are displayed.
-- genres that dont have any shows linked should nkt be displayed
-- only one select statement can be displayed.
SELECT tv_genres.name AS 'genre', COUNT(tv_show_genres.genre_id) AS 'number_of_shows'
FROM tv_genre.id = tv_show_genres.genre_id
GROUP BY genre
ORDER BY number_of_shows DESC;
