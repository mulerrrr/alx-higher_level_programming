#!/usr/bin/python3
"""lists all State objects that contain the letter
a from the database hbtn_0e_6_usa"""

if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import (create_engine)

    # Creates instance of the Database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}\
'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Creates session factory bound to that engine
    Session = sessionmaker(bind=engine)
    # Instance of Session class
    session = Session()
    record = session.query(State).order_by(State.id).filter(State.name.like('\
%a%'))
    for state in record:
        print("{}: {}".format(state.id, state.name))
