-- Create a database
CREATE DATABASE IF NOT EXISTS library_mgmt;
USE library_mgmt;

-- Create a users table
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);

-- Insert user sample data (you can customize this part)
INSERT INTO users (username, password) VALUES
    ('lib-Admin', 'admin'),
    ('lib_Smitty', 'Password@123'),
    ('lib_Lucy', 'Password@3');


-- Create Library Table

CREATE TABLE IF NOT EXISTS library_management (
    Member         varchar(45) NOT NULL,
    PRN_NO         varchar(45) NOT NULL,
    ID             varchar(45) PRIMARY KEY,
    FirstName      varchar(45), 
    LastName       varchar(45), 
    Address1       varchar(45), 
    Address2       varchar(45), 
    PostId         varchar(45), 
    Mobile         varchar(45), 
    BookId         varchar(45), 
    Author         varchar(45), 
    Dateborrowed   varchar(45), 
    datedue        varchar(45), 
    daysofbook     varchar(45), 
    lateretrunfine varchar(45), 
    dateoverdue    varchar(45), 
    finalprice     varchar(45) 
);