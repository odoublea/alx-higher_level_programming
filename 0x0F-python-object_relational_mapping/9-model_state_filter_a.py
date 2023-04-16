#!/usr/bin/python3
'''This module contains a script that lists all the State object that conatain
   the letter `a` from the database hbtn_0e_6_usa with an ORM.
   '''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == '__main__':
    '''This script lists all State objects that contain the letter a from the
       database hbtn_0e_6_usa
       '''
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}')

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()
    states = session.query(State).filter(State.name.like('%a%')).all()

    if (states is None):
        print('Nothing')
    else:
        for state in states:
            print(f'{state.id}: {state.name}')

    session.close()
