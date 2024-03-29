#!/usr/bin/python3
"""Module deletes all objects containing 'a' in their name"""

import sys
from model_state import Base, State


from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]
        ), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State)\
        .filter(State.name.contains('a')).order_by(State.id)

    if states:
        for state in states:
            session.delete(state)

    session.commit()

    # Close the session
    session.close()
