-- all tables without the  genre comedy in the database hbtn_0d_tvshows are listed.
-- database is used to link all rows not linked to one row.
SELECT title
FROM tv_shows
WHERE title NOT IN
(SELECT title
	FROM tv_show
	LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
	LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
	WHERE tv_genres.name ='comedy')
GROUP BY title
ORDER BY title ASC;
