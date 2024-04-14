-- All shows from hbtn-0d-tvshows-rate are shown by their rating
-- All rows of a table by the sum of a linked row are shown.
-- Result must be sorted in ascending order byt the rating.
SELECT title, SUM(tv_show_ratings.rate) 'rating'
FROM tv_show
LEFT JOIN tv_show_ratings ON tv_show_ratings.show_id = tv_show.id
GROUP BY title
ORDER BY rating DESC;
