-- create server test
--   Database hbnb_test_db.
--   grand all privileges to hbnb_test_db to hbnb_test
--   grand select privilege to hbnb_dev on performance_schema

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER
    IF NOT EXISTS 'hbnb_test'@'localhost'
    IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES
   ON `hbnb_test_db`.*
   TO 'hbnb_test'@'localhost'
   IDENTIFIED BY 'hbnb_test_pwd';
GRANT SELECT
   ON `performance_schema`.*
   TO 'hbnb_test'@'localhost'
   IDENTIFIED BY 'hbnb_test_pwd';
FLUSH PRIVILEGES;
