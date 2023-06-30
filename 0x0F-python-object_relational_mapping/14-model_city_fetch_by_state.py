#!/usr/bin/python3
"""Prints all City objects from the database hbtn_0e_14_usa"""


if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from model_city import City
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import relationship

    # Creates instance of the Database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}\
'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Creates session factory bound to that engine
    Session = sessionmaker(bind=engine)
    # Instance of Session class
    session = Session()

    State.cities = relationship("City", back_populates="states")
    record1 = session.query(State.name, City.id, City.name)
    record2 = record1.filter(State.id == City.state_id).order_by(City.id).all()
    for name1, id, name2 in record2:
        print("{}: ({})\
 {}".format(name1, id, name2))
