#!/usr/bin/python3
""" Unittest for AirBnB Amenity class
"""
import unittest
import datetime
import uuid
import os
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """ Tests the Amenity class's methods and attributes. """

    def setUp(self):
        """ sets kwargs properly """
        try:
            os.remove("file.json")
        except:
            pass
        self.amenity1 = Amenity(number=89,
                                created_at="2019-11-13T01:25:18.335269",
                                updated_at="2019-11-13T01:25:18.335279",
                                id="0e5ad480-ebf5-4bc8-9771-2a0e8daff35d")
        self.amenity2 = Amenity()
        self.amenity3 = Amenity()
        self.amenity4 = Amenity(first_name="Betty",
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
            amenity0 = Amenity(number=89)

    def test_init_sufficient_kwargs(self):
        self.assertEqual(self.amenity1.number, 89)
        self.assertEqual(self.amenity1.created_at,
                         datetime.datetime(2019, 11, 13, 1, 25, 18, 335269))
        self.assertEqual(self.amenity1.updated_at,
                         datetime.datetime(2019, 11, 13, 1, 25, 18, 335279))

    def test_init_defaults(self):
        self.assertIs(type(self.amenity2.created_at), datetime.datetime)
        self.assertIs(type(self.amenity3.created_at), datetime.datetime)
        self.assertIs(type(self.amenity2.updated_at), datetime.datetime)
        self.assertIs(type(self.amenity3.updated_at), datetime.datetime)
        self.assertIs(type(self.amenity2.id), str)
        self.assertIs(type(self.amenity3.id), str)
        self.assertNotEqual(self.amenity2.created_at, self.amenity3.created_at)
        self.assertNotEqual(self.amenity2.updated_at, self.amenity3.updated_at)
        self.assertNotEqual(self.amenity2.id, self.amenity3.id)

    def test_str(self):
        self.assertEqual(str(self.amenity1),
                         "[Amenity] ({}) {}".format(
                             "0e5ad480-ebf5-4bc8-9771-2a0e8daff35d",
                             self.amenity1.__dict__))

    def test_str_class_attrs(self):
        self.assertIn('email', self.amenity4.__dict__.keys())
        self.assertIn('password', self.amenity4.__dict__.keys())
        self.assertIn('first_name', self.amenity4.__dict__.keys())
        self.assertIn('last_name', self.amenity4.__dict__.keys())
        self.assertEqual(str(self.amenity4),
                         "[Amenity] ({}) {}".format(
                             "0e5ad480-ebf5-4bc8-9771-2a0e8daff36d",
                             self.amenity4.__dict__))
        self.assertNotIn('email', self.amenity1.__dict__.keys())
        self.assertNotIn('password', self.amenity1.__dict__.keys())
        self.assertNotIn('first_name', self.amenity1.__dict__.keys())
        self.assertNotIn('last_name', self.amenity1.__dict__.keys())
        self.assertNotIn('email', self.amenity2.__dict__.keys())
        self.assertNotIn('password', self.amenity2.__dict__.keys())
        self.assertNotIn('first_name', self.amenity2.__dict__.keys())
        self.assertNotIn('last_name', self.amenity2.__dict__.keys())

    def test_str_instance_attrs(self):
        self.assertNotIn('number', self.amenity2.__dict__.keys())
        self.assertIn('number', self.amenity1.__dict__.keys())

    def test_save(self):
        self.assertEqual(self.amenity1.updated_at,
                         datetime.datetime(2019, 11, 13, 1, 25, 18, 335279))
        self.amenity1.save()
        self.assertNotEqual(self.amenity1.updated_at,
                            datetime.datetime(2019, 11, 13, 1, 25, 18, 335279))
        self.assertEqual(type(self.amenity1.updated_at), datetime.datetime)

    def test_save_instance_attrs(self):
        self.amenity1.save()
        self.assertEqual(self.amenity1.number, 89)

    def test_save_class_attrs(self):
        self.amenity4.save()
        self.assertEqual(self.amenity4.first_name, "Betty")
        self.assertEqual(self.amenity4.last_name, "Holberton")
        self.assertEqual(self.amenity4.email, "airbnb@holbertonschool.com")
        self.assertEqual(self.amenity4.password, "root")

    def test_to_dict(self):
        dict1 = {'number': 89,
                 '__class__': "Amenity",
                 'created_at': "2019-11-13T01:25:18.335269",
                 'updated_at': "2019-11-13T01:25:18.335279",
                 'id': "0e5ad480-ebf5-4bc8-9771-2a0e8daff35d"}
        self.assertEqual(self.amenity1.to_dict(), dict1)

    def test_to_dict_instance_attrs(self):
        self.amenity1.astring = "pew! pew pew!!!"
        self.amenity1.afloat = 9.87654321
        dict1 = {'number': 89,
                 'astring': "pew! pew pew!!!",
                 'afloat': 9.87654321,
                 '__class__': "Amenity",
                 'created_at': "2019-11-13T01:25:18.335269",
                 'updated_at': "2019-11-13T01:25:18.335279",
                 'id': "0e5ad480-ebf5-4bc8-9771-2a0e8daff35d"}
        self.assertEqual(self.amenity1.to_dict(), dict1)

    def test_to_dict_class_attrs(self):
        dict4 = {'first_name': "Betty",
                 'last_name': "Holberton",
                 'email': "airbnb@holbertonschool.com",
                 'password': "root",
                 '__class__': "Amenity",
                 'created_at': "2019-11-13T01:25:18.335289",
                 'updated_at': "2019-11-13T01:25:18.335299",
                 'id': "0e5ad480-ebf5-4bc8-9771-2a0e8daff36d"}
        self.assertEqual(self.amenity4.to_dict(), dict4)
