#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.
Results are sorted by states.id in ascending order.
"""


import MySQLdb
import sys


def list_states(username, password, db_name):
    """Connects to a MySQL database and retriev
    es all rows from the 'states' table.
    The results are sorted in ascending."""
    conn = MySQLdb.connect(
        host="localhost", port=3306, user=username, passwd=password, db=db_name
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    list_states(sys.argv[1], sys.argv[2], sys.argv[3])
