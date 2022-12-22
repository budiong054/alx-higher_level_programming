#!/usr/bin/python3
"""The ``2-my_filter_states.py`` module displays all values in the
    states table of hbtn_0e_0_usa where name matches the argument
"""
import sys
import MySQLdb

if __name__ == '__main__':
    if len(sys.argv) < 5:
        sys.exit(1)
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("""SELECT id, name FROM states WHERE name LIKE %s
                ORDER BY id ASC""", (sys.argv[4],))
    states = cur.fetchall()
    for state in states:
        print(state)
    
    cur.close()
    db.close()
