#!/usr/bin/python3
"""Lists all State objects, and corresponding City objects,
    contained in the database hbtn_0e_101_usa
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine(f"mysql+mysqldb://{user}:{passwd}@localhost/{db}")

    Session = sessionmaker(bind=engine)
    session = Session()
