#!/usr/bin/python3
"""Place module for AirBnB clone"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place class for hbnb.

    @name(str): Place's name
    @city_id(str): will be City.id
    @user_id(str): will be User.id
    @description(str):string - empty string
    @number_rooms(int): default=0
    @number_bathrooms(int): default=0
    @max_guest(int): default=0
    @price_by_night(int): default=0
    @latitude(float): default=0.0
    @longitude(float): default=0.0
    @amenity_ids(list): list of strings, will be list of Amenity.id, default=[]
    """

    name = ""
    city_id = ""
    user_id = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
