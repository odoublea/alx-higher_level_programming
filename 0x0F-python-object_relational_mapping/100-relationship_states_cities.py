#!/usr/bin/python3
'''Script that creates the State “California” with the
City “San Francisco” from the database hbtn_0e_100_usa
'''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State, Base
from relationship_city import City
from sys import argv


if __name__ == '__main__':
    # Get command line arguments
    username, password, database = argv[1:]

    # Create engine and session
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create California state and San Francisco city
    ca = State(name="California")
    sf = City(name="San Francisco", state=ca)

    # Add and commit changes
    session.add(ca)
    session.add(sf)
    session.commit()

    # Close session
    session.close()
