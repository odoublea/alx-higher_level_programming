#!/usr/bin/python3
'''This module contains a script that takes in an argument and displays all
   values in the states table of hbtn_0e_0_usa where name matches the argument.
'''
import MySQLdb
from sys import argv
import re

if __name__ == '__main__':
    '''This script takes in an argument and displays all values in the states
       table of hbtn_0e_0_usa where name matches the argument. But this time,
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
    query = f"SELECT * FROM states WHERE name = BINARY '{searched}' ORDER BY id"

    # Execute the query
    cur.execute(query)

    # Fetch all rows from the query result
    query_rows = cur.fetchall()

    # Print each row
    for row in query_rows:
        print(row)

    # Close the cursor and connection objects
    cur.close()
    conn.close()
