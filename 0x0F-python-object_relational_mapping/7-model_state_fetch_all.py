#!/usr/bin/python3
'''This module contains a script that lists all State objects from the database
   with an ORM'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == '__main__':
    '''This script lists all State objects from the database with an ORM'''
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}')

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()
    selectQuery = session.query(State).order_by(State.id).all()

    for state in selectQuery:
        print(f'{state.id}: {state.name}')

    session.close()
