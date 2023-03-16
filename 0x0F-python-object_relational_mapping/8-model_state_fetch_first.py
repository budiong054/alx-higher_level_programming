#!/usr/bin/python3
"""Prints the first State object from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine(f"mysql+mysqldb://{user}:{passwd}@localhost/{db}")
    Session = sessionmaker(bind=engine)
    session = Session()

    first_state = session.query(State).filter(State.id == 1).first()
    print(f"{first_state.id}: {first_state.name}")
