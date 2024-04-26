#!/usr/bin/python3
""" This Python script deletes all State object that contains the
letter 'a' from the hbtn_0e_6_usa database
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Creating the database engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    # Setting up the tables in the database
    Base.metadata.create_all(engine)
    # Configuring session maker
    Session = sessionmaker(bind=engine)
    session = Session()
    state_obj = session.query(State).filter(
                State.name.like('%a%')).all()
    # Deleting all instances with name containing 'a'
    for state in state_obj:
        session.delete(state)
    # Commiting changes
    session.commit()
    # Closing session maker
    session.close()