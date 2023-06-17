#!/usr/bin/python3
"""List all the states from a database"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # connect to the database
    u = argv[1]
    p = argv[2]
    d = argv[3]
    db = MySQLdb.connect(host="localhost", user=u, passwd=p, db=d, port=3306)
    # get working environment with cursor object
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC;")
    # get all records of the query
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()
