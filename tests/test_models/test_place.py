#!/usr/bin/python3
""" Unittest for AirBnB Place class """
import unittest
import datetime
import uuid
import os
from models.place import Place
from models.engine.file_storage import FileStorage
from models import storage


class TestPlace(unittest.TestCase):
    """ Tests the Place class's methods and attributes. """

    def setUp(self):
        """ sets kwargs properly """
        try:
            os.remove("file.json")
        except:
            pass
        self.place1 = Place(number=89,
                            created_at="2019-11-13T01:25:18.335269",
                            updated_at="2019-11-13T01:25:18.335279",
                            id="0e5ad480-ebf5-4bc8-9771-2a0e8daff35d")
        self.place2 = Place()
        self.place3 = Place()
        self.place4 = Place(first_name="Betty",
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

    def test_attrs(self):
        new = Place(name="Holberton",
                    city_id="tinsletown",
                    user_id="123456789",
                    description="sooooooo shiny",
                    number_rooms=3,
                    number_bathrooms=1,
                    max_guest=35,
                    price_by_night=3000,
                    latitude=12.34,
                    longitude=43.21,
                    amenity_ids=[5, 10, 15],
                    created_at="2019-11-13T01:25:18.335289",
                    updated_at="2019-11-13T01:25:18.335299",
                    id="0e5ad480-ebf5-4bc8-9771-2a0e8daff36d")
        self.assertEqual(new.name, "Holberton")
        self.assertEqual(new.city_id, "tinsletown")
        self.assertEqual(new.user_id, "123456789")
        self.assertEqual(new.description, "sooooooo shiny")
        self.assertEqual(new.number_rooms, 3)
        self.assertEqual(new.number_bathrooms, 1)
        self.assertEqual(new.max_guest, 35)
        self.assertEqual(new.price_by_night, 3000)
        self.assertEqual(new.latitude, 12.34)
        self.assertEqual(new.longitude, 43.21)
        self.assertEqual(new.amenity_ids, [5, 10, 15])

    def test_attrs2(self):
        new = Place()
        self.assertEqual(new.name, "")
        self.assertEqual(new.city_id, "")
        self.assertEqual(new.user_id, "")
        self.assertEqual(new.description, "")
        self.assertEqual(new.number_rooms, 0)
        self.assertEqual(new.number_bathrooms, 0)
        self.assertEqual(new.max_guest, 0)
        self.assertEqual(new.price_by_night, 0)
        self.assertEqual(new.latitude, 0.0)
        self.assertEqual(new.longitude, 0.0)
        self.assertEqual(new.amenity_ids, [])

    def test_init_insufficient_kwargs(self):
        with self.assertRaises(Exception):
            place0 = Place(number=89)

    def test_init_sufficient_kwargs(self):
        self.assertEqual(self.place1.number, 89)
        self.assertEqual(self.place1.created_at,
                         datetime.datetime(2019, 11, 13, 1, 25, 18, 335269))
        self.assertEqual(self.place1.updated_at,
                         datetime.datetime(2019, 11, 13, 1, 25, 18, 335279))

    def test_init_defaults(self):
        self.assertIs(type(self.place2.created_at), datetime.datetime)
        self.assertIs(type(self.place3.created_at), datetime.datetime)
        self.assertIs(type(self.place2.updated_at), datetime.datetime)
        self.assertIs(type(self.place3.updated_at), datetime.datetime)
        self.assertIs(type(self.place2.id), str)
        self.assertIs(type(self.place3.id), str)
        self.assertNotEqual(self.place2.created_at, self.place3.created_at)
        self.assertNotEqual(self.place2.updated_at, self.place3.updated_at)
        self.assertNotEqual(self.place2.id, self.place3.id)

    def test_str(self):
        self.assertEqual(str(self.place1),
                         "[Place] ({}) {}".format(
                             "0e5ad480-ebf5-4bc8-9771-2a0e8daff35d",
                             self.place1.__dict__))

    def test_str_class_attrs(self):
        self.assertIn('email', self.place4.__dict__.keys())
        self.assertIn('password', self.place4.__dict__.keys())
        self.assertIn('first_name', self.place4.__dict__.keys())
        self.assertIn('last_name', self.place4.__dict__.keys())
        self.assertEqual(str(self.place4),
                         "[Place] ({}) {}".format(
                             "0e5ad480-ebf5-4bc8-9771-2a0e8daff36d",
                             self.place4.__dict__))
        self.assertNotIn('email', self.place1.__dict__.keys())
        self.assertNotIn('password', self.place1.__dict__.keys())
        self.assertNotIn('first_name', self.place1.__dict__.keys())
        self.assertNotIn('last_name', self.place1.__dict__.keys())
        self.assertNotIn('email', self.place2.__dict__.keys())
        self.assertNotIn('password', self.place2.__dict__.keys())
        self.assertNotIn('first_name', self.place2.__dict__.keys())
        self.assertNotIn('last_name', self.place2.__dict__.keys())

    def test_str_instance_attrs(self):
        self.assertNotIn('number', self.place2.__dict__.keys())
        self.assertIn('number', self.place1.__dict__.keys())

    def test_save(self):
        self.assertEqual(self.place1.updated_at,
                         datetime.datetime(2019, 11, 13, 1, 25, 18, 335279))
        self.place1.save()
        self.assertNotEqual(self.place1.updated_at,
                            datetime.datetime(2019, 11, 13, 1, 25, 18, 335279))
        self.assertEqual(type(self.place1.updated_at), datetime.datetime)

    def test_save_instance_attrs(self):
        self.place1.save()
        self.assertEqual(self.place1.number, 89)

    def test_save_class_attrs(self):
        self.place4.save()
        self.assertEqual(self.place4.first_name, "Betty")
        self.assertEqual(self.place4.last_name, "Holberton")
        self.assertEqual(self.place4.email, "airbnb@holbertonschool.com")
        self.assertEqual(self.place4.password, "root")

    def test_to_dict(self):
        dict1 = {'number': 89,
                 '__class__': "Place",
                 'created_at': "2019-11-13T01:25:18.335269",
                 'updated_at': "2019-11-13T01:25:18.335279",
                 'id': "0e5ad480-ebf5-4bc8-9771-2a0e8daff35d"}
        self.assertEqual(self.place1.to_dict(), dict1)

    def test_to_dict_instance_attrs(self):
        self.place1.astring = "pew! pew pew!!!"
        self.place1.afloat = 9.87654321
        dict1 = {'number': 89,
                 'astring': "pew! pew pew!!!",
                 'afloat': 9.87654321,
                 '__class__': "Place",
                 'created_at': "2019-11-13T01:25:18.335269",
                 'updated_at': "2019-11-13T01:25:18.335279",
                 'id': "0e5ad480-ebf5-4bc8-9771-2a0e8daff35d"}
        self.assertEqual(self.place1.to_dict(), dict1)

    def test_to_dict_class_attrs(self):
        dict4 = {'first_name': "Betty",
                 'last_name': "Holberton",
                 'email': "airbnb@holbertonschool.com",
                 'password': "root",
                 '__class__': "Place",
                 'created_at': "2019-11-13T01:25:18.335289",
                 'updated_at': "2019-11-13T01:25:18.335299",
                 'id': "0e5ad480-ebf5-4bc8-9771-2a0e8daff36d"}
        self.assertEqual(self.place4.to_dict(), dict4)
