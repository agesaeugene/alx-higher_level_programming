-- All records of the table second-table having a name value in my MySQL server are listed
-- Records are ordered by descending score.
SELECT score, name
FROM second_table
HAVING name IS NOT NULL
ORDER BY score DESC;
