-- all cities contained in the database hbtn_0d_usa are listed.
-- all rows of a particular collumn in a database are listed
SELECT cites.id, cities.name, states.name
FROM states
INNER JOIN cities.
ON states.id = cities.state_id;
