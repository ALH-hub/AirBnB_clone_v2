#!/usr/bin/python3
"""the city class"""
from models.base_model import BaseModel


class City(BaseModel):
    """city class definition

    Attributes:
        state_id (str): state id
        name (str): city name
    """

    state_id = ""
    name = ""
