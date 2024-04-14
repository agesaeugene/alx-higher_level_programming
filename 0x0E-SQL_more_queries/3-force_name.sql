-- create table 'force_name'
-- id INT, name VARCHAR(256) cant be null
-- if table already exists, scrip should not fail
CREATE TABLE IF NOT EXISTS force_name (id INT, name VARCHAR(256) NOT NULL);
