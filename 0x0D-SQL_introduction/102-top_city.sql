-- temp and dataset from ex.18 are used
-- Top 3 cities by temprature during August and July
-- Order by temp descending.
SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE month = 7 OR month = 8
GROUP BY city
ORDER BY avg_tmp DESC
LIMIT 3;
