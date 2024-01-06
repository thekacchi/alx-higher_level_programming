#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Check if all required arguments are provided
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(
              sys.argv[0]))
        sys.exit(1)

    # Get MySQL connection parameters and state name from command line args
    username, password, database, state_name = (
        sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
        )

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the query to fetch and display states with the specified name
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC;".format(
        state_name)
    cursor.execute(query)
    matching_states = cursor.fetchall()

    for state in matching_states:
        print(state)

    # Close cursor and connection
    cursor.close()
    db.close()
