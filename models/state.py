#!/usr/bin/python3
"""State class"""
import models
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from models.city import City
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """state class definition

    Attributes:
        __tablename (str): the name of the sql table
        name (str): name of state
        places (sqlalchemy.relationship): relates states to place
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City",  backref="state", cascade="delete")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """Get a list of all related City objects."""
            city_list = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
