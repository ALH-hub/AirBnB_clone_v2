#!/usr/bin/python3
"""Defines the Place class."""
from models.base_model import BaseModel


class Place(BaseModel):
    """place class definition

    Attributes:
        city_id (str): city id
        user_id (str): user id
        name (str): name of place
        description (str): place description
        number_rooms (int): number of rooms in place
        number_bathrooms (int): number of bathrooms in place
        max_guest (int): max number of guests
        price_by_night (int): price of place by night
        latitude (float): lattitude of place
        longitude (float): longitude of place
        amenity_ids (list): amenities id list
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
