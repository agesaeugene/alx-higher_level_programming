-- all genres in the database hbtn_0d_tvshows_rate are listed according to their rating
-- all rows in a database are linked to a row in another table.
-- Only one select statement can be used.
SELECT name, SUM(tv_show_ratings.rate) 'rating'
FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_show_ratings ON tv_show_genres.show_id = tv_show_ratings.show_id
GROUP BY name
ORDER BY rating DESC;
