#!/usr/bin/python3
"""User class."""
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """Represents a user for a MySQL database

    Attributes:
        __tablename__ (str): table name for user class
        email: (sqlalchemy String): user's email address
        password (sqlalchemy String): user's password
        first_name (sqlalchemy String): user's first name
        last_name (sqlalchemy String): user's last name
        places (sqlalchemy relationship): User-Place relationship
        reviews (sqlalchemy relationship): User-Review relationship
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship("Place", backref="user", cascade="delete")
    reviews = relationship("Review", backref="user", cascade="delete")
