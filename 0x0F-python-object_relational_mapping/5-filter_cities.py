#!/usr/bin/python3
'''This module contains a script that takes in the name of a state as an argument'''
import MySQLdb
from sys import argv
import re

if __name__ == '__main__':
    '''This script takes in the name of a state as an argument and lists all
        cities of that state, using the database hbtn_0e_4_usa.
        it is safe from MySQL injections!
        Args:
             username: MySQL username
             password: MySQL password
             database: MySQL database
             searched: searched state
    '''
    # Get command line arguments
    username = argv[1]
    password = argv[2]
    database = argv[3]
    searched = argv[4]

    # Check length of arguments
    if (len(argv) != 5):
        print('Use: username, password, database name, state name')
        exit(1)

    # Check if search query is valid
    if (re.search('^[a-zA-Z ]+$', searched) is None):
        print('Enter a valid state name (example: Arizona)')
        exit(1)

    # Connect to the MySQL server
    try:
        conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                               passwd=password, db=database, charset="utf8")

    except Exception:
        print('Failed to connect to the database')
        exit(0)

    # Create a cursor object
    cur = conn.cursor()

    # Prepare the SELECT query
    query = f"SELECT cities.name \
              FROM cities \
              JOIN states \
              ON states.id = cities.state_id \
              WHERE states.name = BINARY '{searched}' \
              ORDER BY cities.id"

    # Execute the query
    execQuery = cur.execute(query)

    # Fetch all rows from the query result
    query_rows = cur.fetchall()

    # Print each row
    result = []
    for row in range(execQuery):
        result.append(query_rows[row][0])
        # result.append(row)

    print(', '.join(result))

    # Close the cursor and connection objects
    cur.close()
    conn.close()
