#!/usr/bin/python3
"""
This module retrieves states matching a user-provided name
while protecting against SQL injection, and prints them sorted by id.
"""

import MySQLdb
import sys


def safe_filter_states(username, password, db_name, state_name):
    """
    Connects to MySQL database and prints each record
    matching the user-provided state name, safely parameterized
    to prevent SQL injection.
    """
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=username, passwd=password, db=db_name)
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC",
                (state_name,))
    for row in cur.fetchall():
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    safe_filter_states(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
