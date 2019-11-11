#!/usr/bin/python3
"""base module for AirBnB clone"""
import uuid
import datetime
from models import storage


class BaseModel:
    """base class for this project"""

    def __init__(self, *args, **kwargs):
        """initialization method"""
        if kwargs:
            for k, v in kwargs.items():
                print(k, v)
                setattr(self, k, v)
            self.created_at = datetime.datetime.strptime(self.created_at, '%Y-%m-%dT%H:%M:%S.%f')
            self.updated_at = datetime.datetime.strptime(self.updated_at, '%Y-%m-%dT%H:%M:%S.%f')
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)

    def __str__(self):
        """string rep method"""
        return "[{}] ({}) {}".format("BaseModel", self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at with
        the current datetime"""
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__
        of the instance"""
        mydict = self.__dict__.copy()
        mydict["__class__"] = self.__class__.__name__
        mydict["updated_at"] = self.updated_at.isoformat()
        mydict["created_at"] = self.created_at.isoformat()
        return mydict
