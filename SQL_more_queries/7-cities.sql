-- create database and table and add specific description 
CREATE database IF NOT EXISTS hbtn_0d_usa;
    use hbtn_0d_usa
CREATE table IF NOT EXISTS cities (
    id int AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY,
    state_id INT NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id),
    name VARCHAR(256) NOT NULL
);
