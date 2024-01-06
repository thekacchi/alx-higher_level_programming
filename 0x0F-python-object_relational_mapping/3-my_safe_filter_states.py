#!/usr/bin/python3
"""documentation gies here"""
import MySQLdb
import sys


def fetch_states(username, password, database, state_name):
    try:
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

        # Use parameterized query to fetch and display states with name
        query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC;"
        cursor.execute(query, (state_name,))

        matching_states = cursor.fetchall()

        for state in matching_states:
            print(state)

    except MySQLdb.Error as e:
        print("MySQL Error: {}".format(e))

    finally:
        # Close cursor and connection
        if cursor:
            cursor.close()
        if db:
            db.close()


if __name__ == "__main__":
    # Check if all required arguments are provided
    if len(sys.argv) != 5:
        print(
            "Usage: {} <username> <password> <database> <state_name>".format(
                sys.argv[0]
             )
        )
        sys.exit(1)

    # Get MySQL connection parameters and state name from command line args
    username, password, database, state_name = (
        sys.argv[1],
        sys.argv[2],
        sys.argv[3],
        sys.argv[4]
    )

    fetch_states(username, password, database, state_name)
