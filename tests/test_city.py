#!/usr/bin/python3
""" Unittest for AirBnB City class
"""
import unittest
import datetime
import uuid
import os
from models.city import City


class TestCity(unittest.TestCase):
    """ Tests the City class's methods and attributes. """

    def setUp(self):
        """ sets kwargs properly """
        try:
            os.remove("file.json")
        except:
            pass
        self.city1 = City(number=89,
                          created_at="2019-11-13T01:25:18.335269",
                          updated_at="2019-11-13T01:25:18.335279",
                          id="0e5ad480-ebf5-4bc8-9771-2a0e8daff35d")
        self.city2 = City()
        self.city3 = City()
        self.city4 = City(first_name="Betty",
                          last_name="Holberton",
                          email="airbnb@holbertonschool.com",
                          password="root",
                          created_at="2019-11-13T01:25:18.335289",
                          updated_at="2019-11-13T01:25:18.335299",
                          id="0e5ad480-ebf5-4bc8-9771-2a0e8daff36d")

    def tearDown(self):
        try:
            os.remove("file.json")
        except:
            pass

    def test_init_insufficient_kwargs(self):
        with self.assertRaises(Exception):
            city0 = City(number=89)

    def test_init_sufficient_kwargs(self):
        self.assertEqual(self.city1.number, 89)
        self.assertEqual(self.city1.created_at,
                         datetime.datetime(2019, 11, 13, 1, 25, 18, 335269))
        self.assertEqual(self.city1.updated_at,
                         datetime.datetime(2019, 11, 13, 1, 25, 18, 335279))

    def test_init_defaults(self):
        self.assertIs(type(self.city2.created_at), datetime.datetime)
        self.assertIs(type(self.city3.created_at), datetime.datetime)
        self.assertIs(type(self.city2.updated_at), datetime.datetime)
        self.assertIs(type(self.city3.updated_at), datetime.datetime)
        self.assertIs(type(self.city2.id), str)
        self.assertIs(type(self.city3.id), str)
        self.assertNotEqual(self.city2.created_at, self.city3.created_at)
        self.assertNotEqual(self.city2.updated_at, self.city3.updated_at)
        self.assertNotEqual(self.city2.id, self.city3.id)

    def test_str(self):
        self.assertEqual(str(self.city1),
                         "[City] ({}) {}".format(
                             "0e5ad480-ebf5-4bc8-9771-2a0e8daff35d",
                             self.city1.__dict__))

    def test_str_class_attrs(self):
        self.assertIn('email', self.city4.__dict__.keys())
        self.assertIn('password', self.city4.__dict__.keys())
        self.assertIn('first_name', self.city4.__dict__.keys())
        self.assertIn('last_name', self.city4.__dict__.keys())
        self.assertEqual(str(self.city4),
                         "[City] ({}) {}".format(
                             "0e5ad480-ebf5-4bc8-9771-2a0e8daff36d",
                             self.city4.__dict__))
        self.assertNotIn('email', self.city1.__dict__.keys())
        self.assertNotIn('password', self.city1.__dict__.keys())
        self.assertNotIn('first_name', self.city1.__dict__.keys())
        self.assertNotIn('last_name', self.city1.__dict__.keys())
        self.assertNotIn('email', self.city2.__dict__.keys())
        self.assertNotIn('password', self.city2.__dict__.keys())
        self.assertNotIn('first_name', self.city2.__dict__.keys())
        self.assertNotIn('last_name', self.city2.__dict__.keys())

    def test_str_instance_attrs(self):
        self.assertNotIn('number', self.city2.__dict__.keys())
        self.assertIn('number', self.city1.__dict__.keys())

    def test_save(self):
        self.assertEqual(self.city1.updated_at,
                         datetime.datetime(2019, 11, 13, 1, 25, 18, 335279))
        self.city1.save()
        self.assertNotEqual(self.city1.updated_at,
                            datetime.datetime(2019, 11, 13, 1, 25, 18, 335279))
        self.assertEqual(type(self.city1.updated_at), datetime.datetime)

    def test_save_instance_attrs(self):
        self.city1.save()
        self.assertEqual(self.city1.number, 89)

    def test_save_class_attrs(self):
        self.city4.save()
        self.assertEqual(self.city4.first_name, "Betty")
        self.assertEqual(self.city4.last_name, "Holberton")
        self.assertEqual(self.city4.email, "airbnb@holbertonschool.com")
        self.assertEqual(self.city4.password, "root")

    def test_to_dict(self):
        dict1 = {'number': 89,
                 '__class__': "City",
                 'created_at': "2019-11-13T01:25:18.335269",
                 'updated_at': "2019-11-13T01:25:18.335279",
                 'id': "0e5ad480-ebf5-4bc8-9771-2a0e8daff35d"}
        self.assertEqual(self.city1.to_dict(), dict1)

    def test_to_dict_instance_attrs(self):
        self.city1.astring = "pew! pew pew!!!"
        self.city1.afloat = 9.87654321
        dict1 = {'number': 89,
                 'astring': "pew! pew pew!!!",
                 'afloat': 9.87654321,
                 '__class__': "City",
                 'created_at': "2019-11-13T01:25:18.335269",
                 'updated_at': "2019-11-13T01:25:18.335279",
                 'id': "0e5ad480-ebf5-4bc8-9771-2a0e8daff35d"}
        self.assertEqual(self.city1.to_dict(), dict1)

    def test_to_dict_class_attrs(self):
        dict4 = {'first_name': "Betty",
                 'last_name': "Holberton",
                 'email': "airbnb@holbertonschool.com",
                 'password': "root",
                 '__class__': "City",
                 'created_at': "2019-11-13T01:25:18.335289",
                 'updated_at': "2019-11-13T01:25:18.335299",
                 'id': "0e5ad480-ebf5-4bc8-9771-2a0e8daff36d"}
        self.assertEqual(self.city4.to_dict(), dict4)
