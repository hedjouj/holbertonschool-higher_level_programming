#!/usr/bin/python3
"""
This module lists all cities from a given state name,
safe from SQL injection, printed as comma-separated values sorted by city id.
"""

import MySQLdb
import sys


def filter_cities(username, password, db_name, state_name):
    """
    Connects to MySQL database and prints the names of all cities
    that belong to the specified state name,
    safe from SQL injection and sorted by city id ascending.
    """
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=username, passwd=password, db=db_name)
    cur = conn.cursor()
    cur.execute("""SELECT cities.name FROM cities
                   JOIN states ON cities.state_id = states.id
                   WHERE states.name = %s
                   ORDER BY cities.id ASC""", (state_name,))
    cities = [row[0] for row in cur.fetchall()]
    print(", ".join(cities))
    cur.close()
    conn.close()


if __name__ == "__main__":
    filter_cities(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
