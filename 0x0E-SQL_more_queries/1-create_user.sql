-- Grant all previlages and create  the MYSQL server
CREATE USER
	IF NOT EXISTS 'user_0d_1'@'localhost'
	IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PREVILAGES
ON *.*
TO 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;
