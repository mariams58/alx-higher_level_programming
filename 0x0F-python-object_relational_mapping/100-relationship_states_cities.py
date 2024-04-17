#!/usr/bin/python3
""" This Python script creates the State “California” with
the City “San Francisco” from the database hbtn_0e_100_usa
"""
from sys import argv
from relationship_state import Base, State
from relationship_city import City
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
    # Creating a new State and City Instance
    state = State(name="California")
    city = City(name="San Francisco")
    state.cities.append(city)
    # Adding the new City and State Object to the session
    session.add(state)
    session.add(city)
    # Adding the new state object to the database
    session.commit()
    # Closing session maker
    session.close()
