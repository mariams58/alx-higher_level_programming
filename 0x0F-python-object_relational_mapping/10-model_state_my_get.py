#!/usr/bin/python3
""" This Python script prints State object that has the name
passed as argument from the cli from the hbtn_0e_6_usa database
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
    state_obj = session.query(State).filter(State.name == argv[4]).first()
    if state_obj:
        print(state_obj.id)
    else:
        print("Not found")
    # Closing session maker
    session.close()
