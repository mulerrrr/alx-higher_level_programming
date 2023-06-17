#!/usr/bin/python3
"""Lists all cities of that state, using the database hbtn_0e_4_usa"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    u = argv[1]
    p = argv[2]
    d = argv[3]
    n = argv[4]
    # connect to the database
    db = MySQLdb.connect(host="localhost", user=u, passwd=p, db=d, port=3306)
    # get working environment with cursor object
    cur = db.cursor()
    cur.execute("""SELECT city.name FROM states as state\
    join cities as city
    ON state.id = city.state_id where state.name =%s""", (n, ))
    # get all records of the query
    begin = 0
    for row in cur.fetchall():
        if begin == 0:
            begin += 1
        else:
            print(", ", end='')
        print(row[0], end='')
    print()
    cur.close()
    db.close()
