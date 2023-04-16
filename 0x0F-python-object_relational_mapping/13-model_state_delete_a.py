#!/usr/bin/python3
'''This script contains a script that deletes all State objects with a name
containing the letter `a` from the database hbtn_0e_6_usa
'''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv

if __name__ == '__main__':
    if len(argv) != 4:
        print(f"Usage: username password database")
        exit(1)

    username = argv[1]
    password = argv[2]
    database = argv[3]

    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}'
    )

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()
    state = session.query(State).filter(State.name.like('%a%'))\
        .delete(synchronize_session=False)

    session.commit()
    session.close()
