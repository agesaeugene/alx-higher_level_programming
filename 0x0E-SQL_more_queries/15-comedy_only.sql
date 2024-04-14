-- all comedy shows in the database hbtn_0d_tvshows are shown
-- Rows of a database corresponding to a collumn value are listed
-- all the results should be sorted in ascending order by the show title.
SELECT tvshows.title
FROM tv_shows
INNER JOIN tv_show_genres m ON tv_shows.id = m.show_id
INNER JOIN tv_genres g ON m.genre_id = g.id
WHERE g.name = 'comedy'
ORDEr BY tv_show.title ASC;
