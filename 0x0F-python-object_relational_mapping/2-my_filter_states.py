#!/usr/bin/python3
'''This module contains a script that takes in an argument and
displays all values in the states table of hbtn_0e_0_usa
where name matches the argument.
Args:
    username: MySQL username
    password: MySQL password
    database: MySQL database
    searched: searched state
'''
import MySQLdb
from sys import argv


if __name__ == '__main__':
    # Get command line arguments
    username = argv[1]
    password = argv[2]
    database = argv[3]
    searched = argv[4]

    # Connect to the MySQL server
    try:
        conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                               passwd=password, db=database, charset="utf8")

    except Exception:
        print('Failed to connect to the database')
        exit(0)

    # Create a cursor object
    cur = conn.cursor()

    # SELECT query
    selectQuery = "SELECT * FROM states \
                   WHERE name LIKE BINARY '{}' \
                   ORDER BY id ASC".format(searched)

    # Execute the SELECT query
    cur.execute(selectQuery)

    # Fetch all rows from the query result
    query_rows = cur.fetchall()

    # Print each row
    for row in query_rows:
        print(row)

    # Close the cursor and connection objects
    cur.close()
    conn.close()
