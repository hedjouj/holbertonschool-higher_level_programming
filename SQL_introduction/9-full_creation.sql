-- create a tabe and add multiples rows
CREATE TABLE IF NOT EXISTS second_table(
    id INT,
    name VARCHAR(256),
    score INT
);

insert into second_table (id, name, score) values (1, 'John', 10);
insert into second_table (id, name, score) values (2, 'Alex', 3);
insert into second_table (id, name, score) values (3, 'Bob', 14);
insert into second_table (id, name, score) values (4, 'George', 8);
