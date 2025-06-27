#!/usr/bin/python3
"""
Write a script that lists all
states with a name starting with N
(upper N) from the database hbtn_0e_0_usa
"""


import MySQLdb
import sys



def filter_states(username, password, db_name):
    """
    list states and filter with name starting with N"""
    conn = MySQLdb.connect(
        host="localhost", port=3306, user=username, passwd=password, db=db_name
    )
    cur = conn.cursor()
    query = ("SELECT * FROM states WHERE name ='N%' ORDER by id ASC")
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    filter_states(sys.argv[1], sys.argv[2], sys.argv[3])
