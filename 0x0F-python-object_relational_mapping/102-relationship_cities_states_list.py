#!/usr/bin/python3
"""
Lists all City objects from the database hbtn_0e_101_usa
"""
from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    username, password, database = argv[1:]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(username, password, database),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    st = session.query(State).join(City).order_by(City.id).all()

    for state in st:
        for city in state.cities:
            print("{}: {} -> {}".format(city.id, city.name, state.name))
