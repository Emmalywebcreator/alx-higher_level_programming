#!/usr/bin/python3
"""List all State objects containing `a` from db"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


def list_a_state_obj():
    engine = create_engine("mysql+mysqldb://{}:{}@localhost3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)

    rows = session.query(State).all()

    for i in rows:
        if 'a' in i.__dict__['name']:
            print("{}: {}".format(i.__dict__['id'], i.__dict__['name']))

    session.close()


if __name__ == "__main__":
    list_a_state_obj()
