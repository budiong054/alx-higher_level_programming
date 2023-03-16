#!/usr/bin/python3
"""List all State objects that contain the letter a
   from the database hbtn_0e_6_usa
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

    states_a = session.query(State).filter(State.name.like("%a%"))\
        .order_by(State.id).all()
    for state in states_a:
        print(f"{state.id}: {state.name}")
