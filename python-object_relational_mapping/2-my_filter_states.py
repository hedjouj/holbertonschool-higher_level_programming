#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states
table where name matches the argument.
Usage: ./2-my_filter_states.py <username> <password> <database> <state_name>
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor object
    cursor = db.cursor()

    # WARNING: This is not safe against SQL injection (task 2 only)
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)
    cursor.execute(query)

    # Fetch and print results
    for row in cursor.fetchall():
        print(row)

    # Clean up
    cursor.close()
    db.close()
