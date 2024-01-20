#!/usr/bin/python3
"""the city class"""
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import relationship
from sqlalchemy import Column


class City(BaseModel):
    """city class definition

    Attributes:
        __tablename__: the name of the mysql table
        state_id (sqlalchemy String): state id
        name (sqlalchemy String): foreign key to states.id table
    """

    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
