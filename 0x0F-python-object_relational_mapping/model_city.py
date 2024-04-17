#!/usr/bin/python3
""" State Class definition with declarative base instance
"""
from sqlalchemy.orm import declarative_base
from model_state import Base, State
from sqlalchemy import Column, String, Integer, ForeignKey


class City(Base):
    """ City Class
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
