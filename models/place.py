#!/usr/bin/python3
"""Place class."""
from os import getenv
import models
from models.base_model import Base
from models.base_model import BaseModel
from models.amenity import Amenity
from models.review import Review
from sqlalchemy import Column
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Table
from sqlalchemy.orm import relationship


association_table = Table("place_amenity", Base.metadata,
                          Column("place_id", String(60),
                                 ForeignKey("places.id"),
                                 primary_key=True, nullable=False),
                          Column("amenity_id", String(60),
                                 ForeignKey("amenities.id"),
                                 primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """place class definition/used in db equally

    Attributes:
        __tablename__ (str): table name for place
        city_id (sqlalchemy String): place's city id
        user_id (sqlalchemy String): place's user id
        name (sqlalchemy String): name
        description (sqlalchemy String): description
        number_rooms (sqlalchemy Integer): room numbers
        number_bathrooms (sqlalchemy Integer): bathroom numbers
        max_guest (sqlalchemy Integer): max number of guest
        price_by_night (sqlalchemy Integer): night's price
        latitude (sqlalchemy Float): place's latitude.
        longitude (sqlalchemy Float): place's longitude.
        reviews (sqlalchemy relationship): Place-Review relationship.
        amenities (sqlalchemy relationship): Place-Amenity relationship.
        amenity_list (list): An id list of all linked amenities.
    """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0)
    number_bathrooms = Column(Integer, default=0)
    max_guest = Column(Integer, default=0)
    price_by_night = Column(Integer, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    reviews = relationship("Review", backref="place", cascade="delete")
    amenities = relationship("Amenity", secondary="place_amenity",
                             viewonly=False)
    amenity_list = []

    if getenv("HBNB_TYPE_STORAGE", None) != "db":
        @property
        def reviews(self):
            """list of linked reviews"""
            review_list = []
            for review in list(models.storage.all(Review).values()):
                if review.place_id == self.id:
                    review_list.append(review)
            return review_list

        @property
        def amenities(self):
            """Get/set linked amenities"""
            amenity_list = []
            for amenity in list(models.storage.all(Amenity).values()):
                if amenity.id in self.amenity_list:
                    amenity_list.append(amenity)
            return amenity_list

        @amenities.setter
        def amenities(self, value):
            if type(value) == Amenity:
                self.amenity_list.append(value.id)
