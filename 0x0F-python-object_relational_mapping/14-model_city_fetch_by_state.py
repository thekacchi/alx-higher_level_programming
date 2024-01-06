#!/usr/bin/python3
"""Script to print all City objects from the database hbtn_0e_14_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import Base, City
from model_state import State
from sys import argv


if __name__ == "__main__":
    # Setup connection to MySQL server
    username, password, db_name = argv[1], argv[2], argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, db_name
    ), pool_pre_ping=True)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query and print all City objects sorted by city id
    cities = session.query(City, State).filter(
        City.state_id == State.id
    ).order_by(City.id).all()
    for city, state in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    # Close the session
    session.close()
