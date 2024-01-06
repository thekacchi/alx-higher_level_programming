#!/usr/bin/python3
"""lists all states with a name starting with N (upper N) from the database"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Check if all required arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Get MySQL connection parameters from command line arguments
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the query to fetch and display states starting with 'N'
    cursor.execute(
           "SELECT * FROM states WHERE UPPER(name) LIKE 'N%' ORDER BY id ASC")
    states_with_N = cursor.fetchall()

    for state in states_with_N:
        print(state)

    # Close cursor and connection
    cursor.close()
    db.close()
