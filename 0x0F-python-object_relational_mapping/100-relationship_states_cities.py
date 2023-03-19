#!/usr/bin/python3
"""Creates the State "California" with the City "San Francisco" from
    the database hbtn_0e_100_usa
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

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    california = State(name="California")

    session.add(california)
    session.commit()

    california = session.query(State)\
        .filter(State.name == "California").first()

    san_francisco = City(name="San Francisco", state=california)
    session.add(san_francisco)
    session.commit()
