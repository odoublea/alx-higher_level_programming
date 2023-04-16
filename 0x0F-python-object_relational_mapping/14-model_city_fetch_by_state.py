#!/usr/bin/python3
'''This module contains a script that  prints all City objects
from the database hbtn_0e_14_usa
'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
from sys import argv


if __name__ == '__main__':
    username = argv[1]
    password = argv[2]
    database = argv[3]

    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}',
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()
    for state, city in session.query(State, City).\
            filter(State.id == City.state_id).order_by(City.id).all():
        print(f'{state.name}: ({city.id}) {city.name}')

    session.commit()
    session.close()
