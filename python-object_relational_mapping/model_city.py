#!/usr/bin/python3
"""
This module defines the City model for SQLAlchemy,
mapping the class to the 'cities' table in the database.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """
    City class that maps to the 'cities' table in MySQL,
    with id as primary key, name as non-null string, and state_id
    as a non-null foreign key referencing states.id.
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
