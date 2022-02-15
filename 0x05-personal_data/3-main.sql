-- setup mysql server
-- configure permissions
-- run with the following command:
-- PERSONAL_DATA_DB_USERNAME=root PERSONAL_DATA_DB_PASSWORD=root PERSONAL_DATA_DB_HOST=localhost PERSONAL_DATA_DB_NAME=my_db ./main.py
CREATE DATABASE IF NOT EXISTS my_db;
CREATE USER IF NOT EXISTS root @localhost IDENTIFIED BY 'root';
GRANT ALL PRIVILEGES ON my_db.* TO 'root' @'localhost';
USE my_db;
DROP TABLE IF EXISTS users;
CREATE TABLE users (email VARCHAR(256));
INSERT INTO
  users(email)
VALUES
  ("bob@dylan.com");
INSERT INTO
  users(email)
VALUES
  ("bib@dylan.com");
