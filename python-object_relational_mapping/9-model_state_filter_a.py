#!/usr/bin/python3
"""
This module fetches all State objects from the database containing 'a'
in their name and prints them formatted '<id>: <name>'.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def filter_state_by_a(username, password, db_name):
    """
    Connects via SQLAlchemy and prints records from 'states'
    where the name contains the letter 'a', sorted by id.
    """
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost/{db_name}",
        pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).filter(State.name.like('%a%')).order_by(State.id)
    for state in states:
        print(f"{state.id}: {state.name}")
    session.close()


if __name__ == "__main__":
    filter_state_by_a(sys.argv[1], sys.argv[2], sys.argv[3])
