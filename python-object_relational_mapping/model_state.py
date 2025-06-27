#!/usr/bin/python3
"""
This module defines the State model for SQLAlchemy,
mapping the class to the 'states' table in the database.
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """
    State class that maps to the 'states' table in MySQL,
    with id as primary key and name as non-null string of max length 128.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True)
    name = Column(String(128), nullable=False)
