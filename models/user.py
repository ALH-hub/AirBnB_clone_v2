#!/usr/bin/python3
"""the user class"""
from models.base_model import BaseModel
from sqlalchemy import  Column, String

class User(BaseModel):
    """user class definition

    Attributes:
        email (str): user email
        password (str): user password
        first_name (str): user's first name
        last_name (str): user's last name
    """

    __tablename__ = "users"
    if storage_type == 'db':
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship('place', backref='user', cascade='all, delete-orphan')
        reviews = relationship('Review', backref='user', cascade='all, delete-orphan')
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
