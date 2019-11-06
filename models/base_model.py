#!/usr/bin/python3
"""base module for AirBnB clone"""
import uuid
import datetime


class BaseModel:
    
    """base class for this project"""
    
    def __init__(self, id=None, created_at=None, updated_at=None):

        """initialization method"""
        
        self.id = str(uuid.uuid4())

        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):

        """string rep method"""

        return "[<{}>] (<{}>) <{}>".format("BaseModel", self.id, self.__dict__)


    def save(self):

        """updates the public instance attribute updated_at with
        the current datetime"""

        self.updated_at = datetime.datetime.now()

    def to_dict(self):

        """returns a dictionary containing all keys/values of __dict__
        of the instance"""

        self.updated_at = str(datetime.datetime.isoformat(self.updated_at))
        self.created_at = str(datetime.datetime.isoformat(self.created_at))

        mydict = self.__dict__
        x = {self.__class__ : self}

        x.update(mydict)

        return mydict
