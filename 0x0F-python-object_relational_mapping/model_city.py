#!/usr/bin/python3
"""
SQLAlchemy use
"""


from sqlalchemy import Integer, String, Column, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)

class City(Base):
    """ Class city with id and name attributes """
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
