#!/usr/bin/python3
"""The ``4-cities_by_state`` module lists all cities from the database
    'hbtn_0e_4_usa'
"""
import sys
import MySQLdb

if __name__ == '__main__':
    if len(sys.argv) < 4:
        sys.exit(1)
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name FROM cities
                INNER JOIN states ON states.id = cities.state_id ORDER BY
                cities.id ASC""")
    states = cur.fetchall()
    for state in states:
        print(state)

    cur.close()
    db.close()
