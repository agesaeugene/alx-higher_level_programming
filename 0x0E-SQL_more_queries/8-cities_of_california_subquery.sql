-- all cities of california that can be found on database hbtn-0d_usa are listed.
-- all rows of a collumn in a database are listed.
SELECT id,  name FROM cities WHERE state_id = (SELECT ID FROM states WHERE name = 'california') ORDER BY id ASC;
