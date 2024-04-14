-- all shows containe in hbtn_0_tvshows that have atleast one genre linked are listed.
-- all rows of a database with one collumn in common are listed.
SELECT tv_shows.title, tv_shows_genres.genre_id FROM tv_shows INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
