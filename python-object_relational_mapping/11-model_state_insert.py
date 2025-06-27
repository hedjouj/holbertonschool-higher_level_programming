#!/usr/bin/python3
"""
This module inserts a new State object (Louisiana) into the database
and prints the new record's id.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def insert_state(username, password, db_name):
    """
    Connects to the database using SQLAlchemy, inserts 'Louisiana'
    into 'states', commits, and prints the new id.
    """
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost/{db_name}",
        pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    new = State(name="Louisiana")
    session.add(new)
    session.commit()
    print(new.id)
    session.close()


if __name__ == "__main__":
    insert_state(sys.argv[1], sys.argv[2], sys.argv[3])
