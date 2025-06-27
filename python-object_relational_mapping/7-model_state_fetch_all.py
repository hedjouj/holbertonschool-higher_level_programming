#!/usr/bin/python3
"""
This module fetches all State objects from the database
and prints them in the format '<id>: <name>', ordered by id.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def fetch_all_states(username, password, db_name):
    """
    Connects to the MySQL database using SQLAlchemy
    and prints all State records sorted by id.
    """
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost/{db_name}",
        pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id)
    for state in states:
        print(f"{state.id}: {state.name}")
    session.close()


if __name__ == "__main__":
    fetch_all_states(sys.argv[1], sys.argv[2], sys.argv[3])
