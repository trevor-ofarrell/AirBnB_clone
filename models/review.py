#!/usr/bin/python3
"""Review module for AirBnB clone"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class for hbnb.

    @place_id(str): it will be the Place.id
    @user_id(str): it will be the User.id
    @text(str): default=empty string
    """

    place_id = ""
    user_id = ""
    text = ""
