-- This script will be use to prepare MySQL server for the project.
-- Create data base if not exists with name: hbnb_test_db.
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Create user if not exists with name: hbnb_test and with a password. 
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- Grant all privileges to the hbnb_test.
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
-- Grant the SELECT privilege to hbnb_test.
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';