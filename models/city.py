#!/usr/bin/python3
"""State module for AirBnB clone"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    City class for hbnb.

    @name(str): City's name
    @state_id(str): will be State.id
    """

    name = ""
    state_id = ""
