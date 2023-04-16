#!/usr/bin/python3
'''This module contain a class model_city
'''
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
# from sqlalchemy import create_engine
from model_state import Base, State


class City(Base):
    """
    Class definition of a City
    defines a city by:
        id: integer, auto-generated, primary key
        name: string, 128 characters, nullable
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    def __init__(self, name, state_id):
        self.name = name
        self.state_id = state_id
