#!/usr/bin/python3
"""user class based off of BaseModel"""
from models.base_model import BaseModel

class User(BaseModel):

    email = ""
    password = ""
    first_name = ""
    last_name = ""
