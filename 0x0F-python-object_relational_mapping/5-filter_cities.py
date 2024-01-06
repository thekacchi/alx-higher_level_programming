#!/usr/bin/python3
"""module doc"""

import MySQLdb
import sys


def filter_cities(username, password, database, state_name):
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

# Use parameterized query to fetch and display cities of the specified state
        query = """
        SELECT GROUP_CONCAT(cities.name ORDER BY cities.id ASC SEPARATOR ', ')
        FROM cities
        INNER JOIN states ON cities.state_id = states.id
        WHERE states.name = %s;
        """

        cursor.execute(query, (state_name,))
        cities = cursor.fetchone()

        if cities[0]:
            print(cities[0])

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

# Get MySQL connection parameters and state name from command line arguments
    username, password, database, state_name = (
        sys.argv[1],
        sys.argv[2],
        sys.argv[3],
        sys.argv[4]
    )

    filter_cities(username, password, database, state_name)
