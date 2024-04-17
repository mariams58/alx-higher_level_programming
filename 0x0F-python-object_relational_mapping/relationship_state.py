#!/usr/bin/python3
""" State Class definition with declarative base instance
"""
from sqlalchemy.orm import declarative_base, backref, relationship
from sqlalchemy import Column, String, Integer, MetaData

meta = MetaData()
Base = declarative_base(metadata=meta)


class State(Base):
    """ State Class
    Args (Base) = Base class
    """

    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
