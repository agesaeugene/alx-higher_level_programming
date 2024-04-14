-- create table 'id_notnull'
-- id INT, name VARCHAR(256), default value 1.
-- script should not exist if script should not fail
CREATE TABLE IF NOT EXISTS id_not_null (id INT DEFAULT 1, name VARCHAR(256));
