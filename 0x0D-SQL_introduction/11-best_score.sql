-- All records present in the table second_table with a score >= 10 on my MYSQL server are listed
-- Records are ordered by descending order.
SELECT 'score', 'name'
FROM 'second_table'
WHERE 'score' >= 10
ORDER BY 'score' DESC;
