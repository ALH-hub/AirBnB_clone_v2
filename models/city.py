#!/usr/bin/python3
"""the city class"""
from models.base_model import BaseModel, Base
from models import storage_type
from sqlalchemy import COlumn, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel):
    """city class definition

    Attributes:
        state_id (str): state id
        name (str): city name
    """
    __tablename__ = 'cities':
    if storage_type == 'db':
        name = Column(String(128), nullbale=False)
	stateid = Column(String(60), ForeignKey('states.id'), nullable=False)
	places = relationship('place', backref='cities',
                              cascade='all, delete, delete-orphan')
    state_id = ""
    name = ""
