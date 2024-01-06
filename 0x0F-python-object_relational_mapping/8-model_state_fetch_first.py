#!/usr/bin/python3
"""Print the first State object from the database
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

if __name__ == "__main__":
    # Check if all required arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Get MySQL connection parameters from command line arguments
    username, password, database = (
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]
    )

    # Create an SQLAlchemy engine
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            username, password, database
        ), pool_pre_ping=True
    )

    # Bind the engine to the Base class
    Base.metadata.create_all(engine)

    # Create a session
    session = Session(engine)

    # Query and print the first State object
    first_state = session.query(State).order_by(State.id).first()

    if first_state:
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        print("Nothing")

    # Close the session
    session.close()
