-- all shows contained in the database hbtn_0d_tvshows are listed
-- all rows of tables in a database are listed.
SELECT tv_shows.title, tv_shows_genres.genre_id
FROM tv_shows LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_show.title ASC, tv_show_genres.genre_id ASC;

