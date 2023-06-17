#!/usr/bin/python3
"""Prints the State object with the name passed as
argument from the database hbtn_0e_6_usa"""

if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import (create_engine)
    from sqlalchemy import exc

    # Creates instance of the Database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}\
'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Creates session factory bound to that engine
    Session = sessionmaker(bind=engine)
    # Instance of Session class
    session = Session()
    try:
        record = session.query(State).filter(State.name == sys.argv[4]).one()
        print("{}".format(record.id))
    except exc.SQLAlchemyError:
        print("Not found")
