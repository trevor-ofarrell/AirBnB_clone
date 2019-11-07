#!/usr/bin/python3
import json

"""class that serializes instances to a JSON file
   and deserializes JSON file to instances"""


class FileStorage():
    
    """class to serialize and deserialize classes and json strings"""
    
    __file_path = ""
    __objects = {}

    def all(self):

        """public instance method to return the dictionary __objects"""

        return self.__objects

    def new(self, obj):

        """sets in __objects the obj with key <obj class name>.id"""

        x = {obj: obj.id}
        
        x.update(self._objects)

    def save(self):

        """serializes __objects to the JSON file (path: __file_path)"""

        json.dumps(self.__objects, self.__file_path)

    def reload(self):

        """        deserializes the JSON file to __objects (only if 
        the JSON file (__file_path) exists ; otherwise, do nothing"""

        if self.__file_path:

            __object = json.load(self.__file_path)
        
        else:

            pass
