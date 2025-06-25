-- create database and table and add multiples description 
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
    use     hbtn_0d_usa
CREATE table IF NOT EXISTS states(
    id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);