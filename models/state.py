#!/usr/bin/python3
"""the state class."""
from os import getenv
import models
from models.base_model import BaseModel
from models.base_model import Base
from models.city import City
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import relationship
from sqlalchemy import Column


class State(BaseModel, Base):
    """state class definition

    Attributes:
        __tablename (str): the name of the sql table
        name (str): name of state
        places (sqlalchemy.relationship): relates states to place
    """

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    places = relationship("Place", backref="cities", cascade="delete")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """Get a list of all related City objects."""
            city_list = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
