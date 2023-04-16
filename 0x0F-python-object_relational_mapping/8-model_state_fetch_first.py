#!/usr/bin/python3
'''This module contains a script that lists the first State object from the
   database hbtn_0e_6_usa with an ORM.
   '''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == '__main__':
    '''This script lists the first State object from the database hbtn_0e_6_usa'''
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}')

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()
    state = session.query(State).first()

    if (state is None):
        print('Nothing')
    else:
        print(f'{state.id}: {state.name}')

    session.close()
