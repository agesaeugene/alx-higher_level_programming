-- without a genre connection, lists every program in hbtn_0d_tvshows.
-- all rows that dont have one collumn are listed.
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows,title ASC,  tv_show_genres.genre_id ASC;

