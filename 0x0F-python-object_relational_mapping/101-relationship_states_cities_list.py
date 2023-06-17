#!/usr/bin/python3
"""Prints all City objects from the database hbtn_0e_14_usa"""


if __name__ == "__main__":
    import sys
    from relationship_state import Base, State
    from relationship_city import City
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import relationship

    # Creates instance of the Database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}\
'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    # Creates session factory bound to that engine
    Session = sessionmaker(bind=engine)
    # Instance of Session class
    session = Session()

    record = session.query(State).order_by(State.id)
    for state in record:
        print("{}: {}".format(state.id, state.name))
        for cities in state.cities:
            print("    {}: {}".format(cities.id, cities.name))
