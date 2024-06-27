#!/usr/bin/python3
"""List all State objects containing `a` from db"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from model_state import Base, State


def list_a_state_obj():
    engine = create_engine("mysql+mysqldb://{}:{}@localhost3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    session = Session()
    rows = session.query(State).all()

    for state in session.query(State) \
                        .filter(State.name.ilike('%a%')) \
                        .order_by(State.id.asc()):
        print(f"{state.id}: {state.name}")


if __name__ == "__main__":
    list_a_state_obj()
