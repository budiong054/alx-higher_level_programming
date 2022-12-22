#!/usr/bin/python3
"""The ``1-filter_states.py`` module returns all states with a name
    starting with N from hbtn_0e_0_usa
"""
import sys
import MySQLdb

if __name__ == '__main__':
    if len(sys.argv) < 4:
        sys.exit(1)
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT id, name FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    states = cur.fetchall()
    for state in states:
        print(state)
    
    cur.close()
    db.close()
