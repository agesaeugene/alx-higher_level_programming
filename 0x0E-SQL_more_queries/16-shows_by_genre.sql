-- includes every program from the database hbtn_0d_tvshows, along with every genre that is connected to that show.
-- all rows linked to one anothe in a table are listed.
SELECT title, name
FROM tv_show
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY title ASC, name ASC;
