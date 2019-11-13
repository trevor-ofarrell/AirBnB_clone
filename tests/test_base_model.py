#!/usr/bin/python3
""" Unittest for AirBnB BaseModel class
"""
import unittest
import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ Tests the BaseModel class's methods and attributes. """

    """ sets kwargs properly """
    def setUp(self):
        self.base1 = BaseModel(number=89,
                          created_at="2019-11-13T01:25:18.335269",
                          updated_at="2019-11-13T01:25:18.335279",
                          id="0e5ad480-ebf5-4bc8-9771-2a0e8daff35d")

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
        base2 = BaseModel()
        base3 = BaseModel()
        self.assertIs(type(base2.created_at), datetime.datetime)
        self.assertIs(type(base3.created_at), datetime.datetime)
        self.assertNotEqual(base2, base3)
        

    def test_str(self):
        pass

    def test_str_instance_attrs(self):
        pass

    def test_save(self):
        pass

    def test_save_instance_attrs(self):
        pass

    def test_to_dict(self):
        pass

    def test_to_dict_instance_attrs(self):
        pass
