#!/usr/bin/python3
"""
Write a script that lists all
states with a name starting with N
(upper N) from the database hbtn_0e_0_usa
"""


import MySQLdb
import sys


def list_states(username, password, db_name):
    """
    list states and filter with name starting with N"""
    conn = MySQLdb.connect(
        host="localhost", port=3306, user=username, passwd=password, db=db_name
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE state_name ='N%' ORDER by id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    list_states(sys.argv[1], sys.argv[2], sys.argv[3])
