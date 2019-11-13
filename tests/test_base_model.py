#!/usr/bin/python3
""" Unittest for AirBnB BaseModel class
"""
import unittest
import datetime
import uuid
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ Tests the BaseModel class's methods and attributes. """

    """ sets kwargs properly """
    def setUp(self):
        self.base1 = BaseModel(number=89,
                          created_at="2019-11-13T01:25:18.335269",
                          updated_at="2019-11-13T01:25:18.335279",
                          id="0e5ad480-ebf5-4bc8-9771-2a0e8daff35d")
        self.base2 = BaseModel()
        self.base3 = BaseModel()

    def test_init_insufficient_kwargs(self):
        with self.assertRaises(Exception):
            base0 = BaseModel(number=89)

    def test_init_sufficient_kwargs(self):
        self.assertEqual(self.base1.number, 89)
        self.assertEqual(self.base1.created_at,
                         datetime.datetime(2019, 11, 13, 1, 25, 18, 335269))
        self.assertEqual(self.base1.updated_at,
                         datetime.datetime(2019, 11, 13, 1, 25, 18, 335279))

    def test_init_defaults(self):
        self.assertIs(type(self.base2.created_at), datetime.datetime)
        self.assertIs(type(self.base3.created_at), datetime.datetime)
        self.assertIs(type(self.base2.updated_at), datetime.datetime)
        self.assertIs(type(self.base3.updated_at), datetime.datetime)
        self.assertIs(type(self.base2.id), str)
        self.assertIs(type(self.base3.id), str)
        self.assertNotEqual(self.base2.created_at, self.base3.created_at)
        self.assertNotEqual(self.base2.updated_at, self.base3.updated_at)
        self.assertNotEqual(self.base2.id, self.base3.id)

    def test_str(self):
        self.assertEqual(str(self.base1),
                         "[BaseModel] ({}) {}".format(
                             "0e5ad480-ebf5-4bc8-9771-2a0e8daff35d",
                             self.base1.__dict__))

    def test_str_instance_attrs(self):
        self.assertNotIn('number', self.base2.__dict__.keys())
        self.assertIn('number', self.base1.__dict__.keys())

    def test_save(self):
        pass

    def test_save_instance_attrs(self):
        pass

    def test_to_dict(self):
        pass

    def test_to_dict_instance_attrs(self):
        pass
