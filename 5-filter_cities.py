#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(
        host="localhost", port=3306,
        user=sys.argv[1], passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cur = conn.cursor()
    cur.execute("""SELECT cities.name FROM cities
                   JOIN states ON cities.state_id = states.id
                   WHERE states.name = %s ORDER BY cities.id ASC""", (sys.argv[4],))
    cities = [row[0] for row in cur.fetchall()]
    print(", ".join(cities))
    cur.close()
    conn.close()
