#!/usr/bin/python3
"""
script that lists all states
from the database hbtn_0e_0_usa
"""


import sys
import MySQLdb


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=sys.argv[1],
                           passwd=sys.argv[2],
                           db=sys.argv[3],
                           charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM cities WHERE \
    state_id = (SELECT id FROM state WHERE \
    name = %(name)s)", {'name': sys.argv[4]})
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
