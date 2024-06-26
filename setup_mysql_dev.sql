-- This script will be use to prepare MySQL server for the project.
-- Create data base if not exists with name: hbnb_dev_db.
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Create user if not exists with name: hbnb_dev and with a password. 
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- Grant all privileges to the hbnb_dev.
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- Grant the SELECT privilege to hbnb_de
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';