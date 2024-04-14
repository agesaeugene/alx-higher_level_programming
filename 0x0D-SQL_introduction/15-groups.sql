-- number of records with the same score from the table second_table are listed from MySQL server
-- Records should be orderd in descending order
SELECT score, COUNT(*) AS number
FROM second_table
GROUp BY score
ORDER BY number DESC;
