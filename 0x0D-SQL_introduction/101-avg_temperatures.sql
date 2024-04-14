-- Average temprature by a city imported from DB weather info
-- Order by temprature descending.
SELECT city, avg(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
