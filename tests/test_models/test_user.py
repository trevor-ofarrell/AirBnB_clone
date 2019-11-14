#!/usr/bin/python3
""" Unittest for AirBnB User class """
import unittest
import datetime
import uuid
import os
from models.user import User
from models.engine.file_storage import FileStorage
from models import storage


class TestUser(unittest.TestCase):
    """ Tests the User class's methods and attributes. """

    def setUp(self):
        """ sets kwargs properly """
        try:
            os.remove("file.json")
        except:
            pass
        self.user1 = User(number=89,
                          created_at="2019-11-13T01:25:18.335269",
                          updated_at="2019-11-13T01:25:18.335279",
                          id="0e5ad480-ebf5-4bc8-9771-2a0e8daff35d")
        self.user2 = User()
        self.user3 = User()
        self.user4 = User(first_name="Betty",
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

    def test_instance(self):
        new = User()
        self.assertEqual(new.password, "")
        self.assertEqual(new.first_name, "")
        self.assertEqual(new.last_name, "")
        self.assertEqual(new.email, "")

    def test_instance2(self):
        new = User(
            first_name="Betty",
            last_name="Holberton",
            email="airbnb@holbertonschool.com",
            password="root",
            created_at="2019-11-13T01:25:18.335289",
            updated_at="2019-11-13T01:25:18.335299",
            id="0e5ad480-ebf5-4bc8-9771-2a0e8daff36d")
        self.assertEqual(new.password, "root")
        self.assertEqual(new.last_name, "Holberton")
        self.assertEqual(new.first_name, "Betty")
        self.assertEqual(new.email, "airbnb@holbertonschool.com")

    def test_init_insufficient_kwargs(self):
        with self.assertRaises(Exception):
            user0 = User(number=89)

    def test_init_sufficient_kwargs(self):
        self.assertEqual(self.user1.number, 89)
        self.assertEqual(self.user1.created_at,
                         datetime.datetime(2019, 11, 13, 1, 25, 18, 335269))
        self.assertEqual(self.user1.updated_at,
                         datetime.datetime(2019, 11, 13, 1, 25, 18, 335279))

    def test_init_defaults(self):
        self.assertIs(type(self.user2.created_at), datetime.datetime)
        self.assertIs(type(self.user3.created_at), datetime.datetime)
        self.assertIs(type(self.user2.updated_at), datetime.datetime)
        self.assertIs(type(self.user3.updated_at), datetime.datetime)
        self.assertIs(type(self.user2.id), str)
        self.assertIs(type(self.user3.id), str)
        self.assertNotEqual(self.user2.created_at, self.user3.created_at)
        self.assertNotEqual(self.user2.updated_at, self.user3.updated_at)
        self.assertNotEqual(self.user2.id, self.user3.id)

    def test_str(self):
        self.assertEqual(str(self.user1),
                         "[User] ({}) {}".format(
                             "0e5ad480-ebf5-4bc8-9771-2a0e8daff35d",
                             self.user1.__dict__))

    def test_str_class_attrs(self):
        self.assertIn('email', self.user4.__dict__.keys())
        self.assertIn('password', self.user4.__dict__.keys())
        self.assertIn('first_name', self.user4.__dict__.keys())
        self.assertIn('last_name', self.user4.__dict__.keys())
        self.assertEqual(str(self.user4),
                         "[User] ({}) {}".format(
                             "0e5ad480-ebf5-4bc8-9771-2a0e8daff36d",
                             self.user4.__dict__))
        self.assertNotIn('email', self.user1.__dict__.keys())
        self.assertNotIn('password', self.user1.__dict__.keys())
        self.assertNotIn('first_name', self.user1.__dict__.keys())
        self.assertNotIn('last_name', self.user1.__dict__.keys())
        self.assertNotIn('email', self.user2.__dict__.keys())
        self.assertNotIn('password', self.user2.__dict__.keys())
        self.assertNotIn('first_name', self.user2.__dict__.keys())
        self.assertNotIn('last_name', self.user2.__dict__.keys())

    def test_str_instance_attrs(self):
        self.assertNotIn('number', self.user2.__dict__.keys())
        self.assertIn('number', self.user1.__dict__.keys())

    def test_save(self):
        self.assertEqual(self.user1.updated_at,
                         datetime.datetime(2019, 11, 13, 1, 25, 18, 335279))
        self.user1.save()
        self.assertNotEqual(self.user1.updated_at,
                            datetime.datetime(2019, 11, 13, 1, 25, 18, 335279))
        self.assertEqual(type(self.user1.updated_at), datetime.datetime)

    def test_save_instance_attrs(self):
        self.user1.save()
        self.assertEqual(self.user1.number, 89)

    def test_save_class_attrs(self):
        self.user4.save()
        self.assertEqual(self.user4.first_name, "Betty")
        self.assertEqual(self.user4.last_name, "Holberton")
        self.assertEqual(self.user4.email, "airbnb@holbertonschool.com")
        self.assertEqual(self.user4.password, "root")

    def test_to_dict(self):
        dict1 = {'number': 89,
                 '__class__': "User",
                 'created_at': "2019-11-13T01:25:18.335269",
                 'updated_at': "2019-11-13T01:25:18.335279",
                 'id': "0e5ad480-ebf5-4bc8-9771-2a0e8daff35d"}
        self.assertEqual(self.user1.to_dict(), dict1)

    def test_to_dict_instance_attrs(self):
        self.user1.astring = "pew! pew pew!!!"
        self.user1.afloat = 9.87654321
        dict1 = {'number': 89,
                 'astring': "pew! pew pew!!!",
                 'afloat': 9.87654321,
                 '__class__': "User",
                 'created_at': "2019-11-13T01:25:18.335269",
                 'updated_at': "2019-11-13T01:25:18.335279",
                 'id': "0e5ad480-ebf5-4bc8-9771-2a0e8daff35d"}
        self.assertEqual(self.user1.to_dict(), dict1)

    def test_to_dict_class_attrs(self):
        dict4 = {'first_name': "Betty",
                 'last_name': "Holberton",
                 'email': "airbnb@holbertonschool.com",
                 'password': "root",
                 '__class__': "User",
                 'created_at': "2019-11-13T01:25:18.335289",
                 'updated_at': "2019-11-13T01:25:18.335299",
                 'id': "0e5ad480-ebf5-4bc8-9771-2a0e8daff36d"}
        self.assertEqual(self.user4.to_dict(), dict4)
