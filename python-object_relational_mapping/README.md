# Python - Object-relational mapping

This project is part of the Higher Level Programming curriculum at Holberton School.  
Its purpose is to learn how to interact with a MySQL database using Python and the MySQLdb and SQLAlchemy modules.

## 📚 Learning Objectives

- Understand what Object Relational Mapping (ORM) is and why it's useful.
- Connect a Python script to a MySQL database using `MySQLdb`.
- Use `SQLAlchemy` to map Python classes to MySQL tables.
- Perform basic SQL operations (SELECT, INSERT, UPDATE, DELETE) in Python.
- Avoid SQL injection by using parameterized queries.
- Understand the difference between executing raw SQL and using an ORM.

## 🛠️ Technologies

- Python 3.8.5
- MySQL 8.x
- Ubuntu 20.04 LTS
- `MySQLdb` version 2.0.x
- `SQLAlchemy` version 1.4.x
- Pycodestyle 2.7.*

## 📁 Files

| Filename              | Description                                      |
|-----------------------|--------------------------------------------------|
| `0-select_states.py`  | Lists all states from the database.              |
| `1-filter_states.py`  | Lists all states with names starting with 'N'.   |
| `2-my_filter_states.py` | Filters by user-provided state name.         |
| ...                   | ... (and so on for each task)                    |

## 🚀 Usage

All scripts are executable and take command line arguments:

```bash
./0-select_states.py <mysql_username> <mysql_password> <database_name>
