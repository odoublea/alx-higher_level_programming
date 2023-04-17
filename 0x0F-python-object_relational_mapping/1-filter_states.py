#!/usr/bin/python3
'''This module contains a script that lists all states with a
   name starting `N` from the database hbtn_0e_0_usa with without ORM
   '''
import MySQLdb
from sys import argv


if __name__ == '__main__':
    # Get command line arguments
    username = argv[1]
    password = argv[2]
    database = argv[3]

    if len(argv) != 4:
        print("Usage: username password database")
        exit(1)

    # Connect to the MySQL server
    try:
        conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                               passwd=password, db=database, charset="utf8")

    except Exception:
        print('Failed to connect to the database')
        exit(1)

    # Create a cursor object
    cur = conn.cursor()

    # SELECT query
    selectQuery = f"SELECT * FROM states \
                    WHERE  CONVERT(`name` USING Latin1) \
                    COLLATE Latin1_General_CS LIKE 'N%' \
                    ORDER BY states.id ASC"

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
