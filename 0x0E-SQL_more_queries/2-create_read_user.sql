--Databse hbtn_0d_2 and the user user_0d_2 are created.
--creates a databse.
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
--creating user 'user_0d_2'
CREATE USER IF NOT EXISTS user_0d_2@localhost IDENTIFIED BY 'user_0d_2_pwd';
--selecting grant previlages for a user.
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d__2'@'localhost';
FLUSH PRIVILEGES;
