#!/usr/bin/python3
"""
This module deletes all State objects whose names contain the letter 'a'.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def delete_states_with_a(username, password, db_name):
    """
    Connects via SQLAlchemy and deletes every State record
    with names containing 'a', then commits the transaction.
    """
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost/{db_name}",
        pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query
    (State).filter(State.name.like('%a%')).delete(synchronize_session='fetch')
    session.commit()
    session.close()


if __name__ == "__main__":
    delete_states_with_a(sys.argv[1], sys.argv[2], sys.argv[3])
