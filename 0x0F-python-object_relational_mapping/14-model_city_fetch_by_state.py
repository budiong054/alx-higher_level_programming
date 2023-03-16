#!/usr/bin/python3
"""Prints all City objects from the database hbtn_0e_14_usa
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine(f"mysql+mysqldb://{user}:{passwd}@localhost/{db}")
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State.name, City.id, City.name)\
        .join(City).order_by(City.id).all()
    for state in states:
        print(f"{state[0]}: ({state[1]}) {state[2]}")
