#!/usr/bin/python3
"""list all cities in table"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Check if all required arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Get MySQL connection parameters from command line arguments
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

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

# Execute a query to fetch and display cities with corresponding state names
        query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        INNER JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC;
        """

        cursor.execute(query)
        cities = cursor.fetchall()

        for city in cities:
            print(city)

    except MySQLdb.Error as e:
        print("MySQL Error: {}".format(e))

    finally:
        # Close cursor and connection
        if cursor:
            cursor.close()
        if db:
            db.close()
