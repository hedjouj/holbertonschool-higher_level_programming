#!/usr/bin/python3
"""
This module lists all cities from the 'cities' table along with their state name,
sorted by city id in ascending order, using a single execute() call.
"""

import MySQLdb
import sys


def cities_by_state(username, password, db_name):
    """
    Connects to MySQL database and prints each city record as tuple
    (city_id, city_name, state_name), joined with its state,
    sorted by city id ascending.
    """
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=username, passwd=password, db=db_name)
    cur = conn.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name
                   FROM cities JOIN states
                   ON cities.state_id = states.id
                   ORDER BY cities.id ASC""")
    for row in cur.fetchall():
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    cities_by_state(sys.argv[1], sys.argv[2], sys.argv[3])
