#!/usr/bin/python3
'''This module contains a script that lists all states from the database
   hbtn_0e_0_usa

'''
import MySQLdb
from sys import argv

if __name__ == '__main__':
    '''This script lists all states from the database hbtn_0e_0_usa'''
    # Get command line arguments
    username = argv[1]
    password = argv[2]
    database = argv[3]

    # Connect to the MySQL server
    try:
        conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                               passwd=password, db=database, charset="utf8")

    except Exception:
        print('Failed to connect to the database')
        exit(0)

    # Create a cursor object
    cur = conn.cursor()

    # Execute the SELECT query
    # HERE I have to know SQL to grab all states in my database
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all rows from the query result
    query_rows = cur.fetchall()

    # Print each row
    for row in query_rows:
        print(row)

    # Close the cursor and connection objects
    cur.close()
    conn.close()
