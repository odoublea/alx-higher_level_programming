#!/usr/bin/python3
"""
Contains the class definition of a State
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    Class definition of a State
    defines a state by:
        id: integer, auto-generated, primary key
        name: string, 128 characters, nullable
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
