#!/usr/bin/python3
"""List all the states from a database beginning by N"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    u = argv[1]
    p = argv[2]
    d = argv[3]
    # connect to the database
    db = MySQLdb.connect(host="localhost", user=u, passwd=p, db=d, port=3306)
    # get working environment with cursor object
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name\
    LIKE BINARY 'N%' ORDER BY id ASC")
    # get all records of the query
    records = cur.fetchall()
    for row in records:
        print(row)
    cur.close()
    db.close()
