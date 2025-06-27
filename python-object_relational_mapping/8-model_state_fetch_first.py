#!/usr/bin/python3
"""
This module fetches the first State object from the database ordered by id
and prints it as '<id>: <name>'. Prints 'Nothing' if no record.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def fetch_first_state(username, password, db_name):
    """
    Connects to MySQL via SQLAlchemy and retrieves the first State record.
    Outputs 'Nothing' if the table is empty.
    """
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost/{db_name}",
        pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    first = session.query(State).order_by(State.id).first()
    print(f"{first.id}: {first.name}" if first else "Nothing")
    session.close()


if __name__ == "__main__":
    fetch_first_state(sys.argv[1], sys.argv[2], sys.argv[3])
