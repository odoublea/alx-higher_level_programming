#!/usr/bin/python3
'''This module contains a script that changes the name of a State object
from the database hbtn_0e_6_usa.
'''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv

if __name__ == '__main__':
    if len(argv) != 4:
        print(f"Usage: username password database")
        sys.exit(1)

    username = argv[1]
    password = argv[2]
    database = argv[3]

    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}'
    )

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()

    state = session.query(State).filter(State.id == 2).first()

    if state is None:
        print("State with id=2 not found")
        exit(1)

    state.name = "New Mexico"

    session.commit()
    session.close()
