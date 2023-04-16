#!/usr/bin/python3
'''This module contains a script that adds the State object'''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv

if __name__ == '__main__':
    username = argv[1]
    password = argv[2]
    database = argv[3]

    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}'
    )

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()
    newState = State('Louisiana')

    session.add(newState)

    querySelect = session.query(State).filter(State.name == 'Louisiana')

    for row in querySelect:
        print(row.id)

    session.commit()
    session.close()
