#!/usr/bin/python3
'''This module contains a script that lists all the State object that conatain
   the letter `a` from the database hbtn_0e_6_usa with an ORM.
   '''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv
import re

if __name__ == '__main__':
    '''This script lists all State objects that contain the letter a from the
       database hbtn_0e_6_usa
       '''
    username = argv[1]
    password = argv[2]
    database = argv[3]
    searched = argv[4]

    if (len(argv) != 5):
        print('Use: username, password, database_name, state')
        exit(1)

    if (re.search('^[a-zA-Z ]+$', searched) is None):
        print('Enter a valid name state (example: Arizona)')
        exit(1)

    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}')

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()
    state = session.query(State).filter(State.name == f'{searched}')

    if (state.count() == 0):
        print('Not found')
    else:
        for row in state:
            print(row.id)

    session.close()
