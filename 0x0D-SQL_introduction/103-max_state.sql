-- using same data from ex.18
-- Max temprature of each state is displayed
SELECT state, MAX(value) AS max_temp
FROM temperatures
GROUP BY state
LIMIT 3;
