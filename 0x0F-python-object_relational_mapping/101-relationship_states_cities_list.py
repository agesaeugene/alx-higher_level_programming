#!/usr/bin/python3
"""
Python script that lists all State objects, and corresponding City objects, contained in the database
"""

import sys
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

# Define the base class
Base = declarative_base()

# Define the City class
class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    name = Column(String(256), nullable=False)

    state = relationship("State", back_populates="cities")

# Define the State class
class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(256), nullable=False)

    cities = relationship("City", back_populates="state")

# Main script
inp = sys.argv
if len(inp) < 4:
    exit(1)

conn_str = "mysql+mysqldb://{}:{}@localhost:3306/{}"
engine = create_engine(conn_str.format(inp[1], inp[2], inp[3]))
Session = sessionmaker(bind=engine)

Base.metadata.create_all(engine)

session = Session()
my_query = session.query(State).order_by(State.id).all()
for state in my_query:
    print("{}: {}".format(state.id, state.name))
    for city in state.cities:
        print("\t{}: {}".format(city.id, city.name))

session.close()

