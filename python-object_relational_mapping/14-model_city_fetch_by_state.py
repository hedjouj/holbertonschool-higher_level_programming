#!/usr/bin/python3
"""
This module lists all City objects along with their state names
in the format '<state name>: (<city id>) <city name>' sorted by city id.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
import sys


def fetch_cities_by_state(username, password, db_name):
    """
    Connects via SQLAlchemy and prints each City record
    joined with its State, in the format specified,
    sorted by city id in ascending order.
    """
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost/{db_name}",
        pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(City, State).join(State).order_by(City.id)
    for city, state in result:
        print(f"{state.name}: ({city.id}) {city.name}")
    session.close()


if __name__ == "__main__":
    fetch_cities_by_state(sys.argv[1], sys.argv[2], sys.argv[3])
