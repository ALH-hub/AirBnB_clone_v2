-- prepare MYSQL server for the project.
-- new user hbnb_test in local host
-- user has all privileges.

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
USE hbnb_test;
CREATE USER IF NOT EXISTS 'hbnb_test'@'loacalhost' IDENTIFIED BY 'hbnb_test_pwd';

-- grant all privileges to hbnb_test_db
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;

-- grant privileges to perfomance schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES
