#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import os
import pathlib


class TestFileStorage(unittest.TestCase):
    """ Tests the FileStorage class's methods and attributes. """

    def setUp(self):
        try:
            os.remove("file.json")
        except:
            pass
        storage.__class__._FileStorage__objects = {}

    def tearDown(self):
        try:
            os.remove("file.json")
        except:
            pass
        storage.__class__._FileStorage__objects = {}

    def test_all_empty(self):
        """test if empty dict"""
        self.assertIs(type(storage.all()), dict)
        self.assertEqual(storage.all(), {})

    def test_all(self):
        """test all"""
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        my_model.save()
        self.assertEqual(type(storage.all()), dict)

    def test_all_instance_attrs(self):
        """test attrs"""
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        my_model.save()
        self.assertIsInstance(storage.all(), dict)

    def test_new_empty(self):
        new = BaseModel()
        self.assertEqual(storage.new(new), None)

    def test_new(self):
        new = BaseModel()
        new.name = "Holberton"
        new.my_number = 89
        new.save()
        self.assertEqual(type(storage.all()), dict)

    def test_new_bad_obj(self):
        """tests for lacking class.__name__ and lacking .id"""
        new = BaseModel()
        new.name = "Holberton"
        new.my_number = 89

    def test_save_single_obj(self):
        storage.new(BaseModel())
        storage.save()
        l = []
        num = len(storage.all())
        l.append(num)
        fr = frozenset(l)
        newl = list(fr)
        self.assertEqual(int(newl[0]), 1)

    def test_save_first(self):
        new = BaseModel()
        new.name = "Holberton"
        new.my_number = 89
        new.save()
        with open('file.json', 'r') as f:
            nstr = str(storage.all()).split('-')
            nstr2 = str(f.read()).split('-')
            self.assertEqual(nstr[0][2:], nstr2[0][2:])

    def test_save_additional(self):
        storage.new(BaseModel())
        storage.save()
        all_objs = storage.all()
        for obj_id in all_objs.keys():
            obj = all_objs[obj_id]
        nobj = BaseModel()
        nobj.save()
        obj2 = str(obj).split(' ')
        nobj2 = str(nobj).split(' ')
        self.assertEqual(obj2[0], nobj2[0])

    def test_save_multiple_objs(self):
        storage.new(BaseModel())
        storage.new(BaseModel())
        storage.new(BaseModel())
        storage.save()
        l = []
        num = len(storage.all())
        l.append(num)
        fr = frozenset(l)
        new = BaseModel()
        new2 = BaseModel()
        new3 = BaseModel()
        new4 = BaseModel()
        newl = list(fr)
        self.assertEqual(int(newl[0]), 3)

    def test_reload_file_nonexist(self):
        pass

    def test_reload(self):
        model = BaseModel()
        model.save()
        storage.__class__._FileStorage__objects = {}
        storage.reload()
        oblist = []
        all_objs = storage.all()
        for obj_id in all_objs.keys():
            obj = all_objs[obj_id]
            oblist.append(obj)
        self.assertIs(type(oblist[0]), type(BaseModel()))

if __name__ == "__main__":
    unittest.main()
