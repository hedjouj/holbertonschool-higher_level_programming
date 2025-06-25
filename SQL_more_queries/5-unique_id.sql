-- create a table add description 
CREATE table IF NOT EXISTS unique_id(
    id INT default 1 UNIQUE,
    name VARCHAR(256)
);
