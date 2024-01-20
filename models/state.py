#!/usr/bin/python3
"""the state class."""
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import relationship
from sqlalchemy import Column

class State(BaseModel):
    """state class definition

    Attributes:
        __tablename (str): the name of the sql table
        name (str): name of state
        places (sqlalchemy.relationship): the relationship between States and Place
    """

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    places = relationship("Place", backref="cities", cascade="delete")
