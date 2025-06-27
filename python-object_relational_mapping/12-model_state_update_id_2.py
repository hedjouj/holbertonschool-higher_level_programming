#!/usr/bin/python3
"""
This module updates the State object with id=2 to have the name 'New Mexico'.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def update_state_id_2(username, password, db_name):
    """
    Connects via SQLAlchemy, retrieves State with id 2,
    updates its name to 'New Mexico' and commits the change.
    """
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost/{db_name}",
        pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.get(State, 2)
    if state:
        state.name = "New Mexico"
        session.commit()
    session.close()


if __name__ == "__main__":
    update_state_id_2(sys.argv[1], sys.argv[2], sys.argv[3])
