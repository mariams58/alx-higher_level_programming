#!/usr/bin/python3
""" This Python script lists all City object from the
hbtn_0e_6_usa database
"""
from sys import argv
from model_state import Base, State
from model_city import City
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
    city_obj = session.query(City, State).filter(
                City.state_id == State.id).all()
    # Printing instances in City table with specified format
    for city in city_obj:
        print("{}: ({}) {}".format(city[1].name, city[0].id, city[0].name))
    # Commiting changes
    session.commit()
    # Closing session maker
    session.close()
