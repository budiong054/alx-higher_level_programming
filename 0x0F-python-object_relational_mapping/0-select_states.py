#!/usr/bin/python3
"""The ``0-select_states`` module
"""
import MySQLdb
import sys

if __name__ == '__main__':
    if len(sys.argv) < 4:
        sys.exit(1)
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT id, name FROM states ORDER BY id ASC")
    allstates = cur.fetchall()
    for state in allstates:
        print("{}".format(state))

    cur.close()
    db.close()
