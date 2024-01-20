#!/usr/bin/python3
"""Review class."""
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import relationship


class Review(BaseModel, Base):
    """review for database

    Attributes:
        __tablename__ (str): review table name
        text (sqlalchemy String): review description
        place_id (sqlalchemy String): review place id
        user_id (sqlalchemy String): review user id
    """
    __tablename__ = "reviews"
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
