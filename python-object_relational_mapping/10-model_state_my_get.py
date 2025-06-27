#!/usr/bin/python3
"""
This module prints the id of the State object that matches a given name.
If not found, prints 'Not found'.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def get_state_by_name(username, password, db_name, state_name):
    """
    Uses SQLAlchemy to find the State object by name (safe),
    prints its id or 'Not found' if no match.
    """
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost/{db_name}",
        pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).filter(State.name == state_name).first()
    print(state.id if state else "Not found")
    session.close()


if __name__ == "__main__":
    get_state_by_name(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
