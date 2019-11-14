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

    def tearDown(self):
        try:
            os.remove("file.json")
        except:
            pass

    def test_all_empty(self):
        """test if empty dict"""
        self.assertEqual(type(storage.all()), dict)

    def test_save_single_obj(self):
        l = []
        if os.path.exists('file.json'):
            os.remove('file.json')
        num = len(storage.all())
        l.append(num)
        fr = frozenset(l)
        new = BaseModel()
        newl = list(fr)
        self.assertEqual(int(newl[0]), 77)

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
        all_objs = storage.all()
        for obj_id in all_objs.keys():
            obj = all_objs[obj_id]
        nobj = BaseModel()
        nobj.save()
        obj2 = str(obj).split(' ')
        nobj2 = str(nobj).split(' ')
        self.assertEqual(obj2[0], nobj2[0])

    def test_save_multiple_objs(self):
        if os.path.exists('file.json'):
            os.remove('file.json')
        l = []
        num = len(storage.all())
        l.append(num)
        fr = frozenset(l)
        new = BaseModel()
        new2 = BaseModel()
        new3 = BaseModel()
        new4 = BaseModel()
        newl = list(fr)
        self.assertEqual(int(newl[0]), 73)

    def test_reload_file_nonexist(self):
        pass

    def test_reload(self):
        oblist = []
        all_objs = storage.all()
        for obj_id in all_objs.keys():
            obj = all_objs[obj_id]
            oblist.append(obj)
        self.assertEqual(type(oblist[0]), type(BaseModel())) 

    def test_reload_class_nonexist(self):
        oblist = []
        all_objs = storage.all()
        for obj_id in all_objs.keys():
            obj = all_objs[obj_id]
            oblist.append(obj)
        self.assertEqual()

    def test_reload_not_json(self):
        pass

if __name__ == "__main__":
    unittest.main()
