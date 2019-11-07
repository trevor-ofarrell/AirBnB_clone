#!/usr/bin/python3
import json
import os.path
from os import path

"""class that serializes instances to a JSON file
   and deserializes JSON file to instances"""


class FileStorage():
    
    """class to serialize and deserialize classes and json strings"""
    
    __file_path = "file.json"
    __objects = {}

    def all(self):

        """public instance method to return the dictionary __objects"""

        return self.__objects

    def new(self, obj):

        """sets in __objects the obj with key <obj class name>.id"""

        x = { "{}.{}".format(obj.__class__.__name__, obj.id): obj.to_dict() }
        
        x.update(self.__objects)

    def save(self):

        """serializes __objects to the JSON file (path: __file_path)"""

        with open(self.__file_path, 'w+') as outfile:
        
            print(self.__objects)
            
            json.dump(self.__objects, outfile)

    def reload(self):

        """        deserializes the JSON file to __objects (only if 
        the JSON file (__file_path) exists ; otherwise, do nothing"""

        if path.exists(self.__file_path):
            
            with open(self.__file_path, 'r') as json_file:

                self.__object = json.load(json_file)
        
        else:

            pass
