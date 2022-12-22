#!/usr/bin/python3
"""The ``5-filter_cities`` module takes in the name of a states as an
    argument and lists all cities of that state, using the database
    'hbtn_0e_4_usa'
"""
import sys
import MySQLdb

if __name__ == '__main__':
    if len(sys.argv) < 5:
        sys.exit(1)
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("""SELECT cities.name FROM cities INNER JOIN states
                ON states.id = cities.state_id WHERE states.name LIKE %s
                ORDER BY cities.id ASC""", (sys.argv[4],))
    cities = cur.fetchall()
    j = 0
    for city in cities:
        for i in city:
            if j == 0:
                print("{}".format(i), end="")
                j += 1
                continue
            print(", {}".format(i), end="")
    print()

    cur.close()
    db.close()
