#!/usr/bin/python3
""" Unittest for AirBnB Review class
"""
import unittest
import datetime
import uuid
import os
from models.review import Review


class TestReview(unittest.TestCase):
    """ Tests the Review class's methods and attributes. """

    def setUp(self):
        """ sets kwargs properly """
        try:
            os.remove("file.json")
        except:
            pass
        self.review1 = Review(number=89,
                              created_at="2019-11-13T01:25:18.335269",
                              updated_at="2019-11-13T01:25:18.335279",
                              id="0e5ad480-ebf5-4bc8-9771-2a0e8daff35d")
        self.review2 = Review()
        self.review3 = Review()
        self.review4 = Review(first_name="Betty",
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
            review0 = Review(number=89)

    def test_init_sufficient_kwargs(self):
        self.assertEqual(self.review1.number, 89)
        self.assertEqual(self.review1.created_at,
                         datetime.datetime(2019, 11, 13, 1, 25, 18, 335269))
        self.assertEqual(self.review1.updated_at,
                         datetime.datetime(2019, 11, 13, 1, 25, 18, 335279))

    def test_init_defaults(self):
        self.assertIs(type(self.review2.created_at), datetime.datetime)
        self.assertIs(type(self.review3.created_at), datetime.datetime)
        self.assertIs(type(self.review2.updated_at), datetime.datetime)
        self.assertIs(type(self.review3.updated_at), datetime.datetime)
        self.assertIs(type(self.review2.id), str)
        self.assertIs(type(self.review3.id), str)
        self.assertNotEqual(self.review2.created_at, self.review3.created_at)
        self.assertNotEqual(self.review2.updated_at, self.review3.updated_at)
        self.assertNotEqual(self.review2.id, self.review3.id)

    def test_str(self):
        self.assertEqual(str(self.review1),
                         "[Review] ({}) {}".format(
                             "0e5ad480-ebf5-4bc8-9771-2a0e8daff35d",
                             self.review1.__dict__))

    def test_str_class_attrs(self):
        self.assertIn('email', self.review4.__dict__.keys())
        self.assertIn('password', self.review4.__dict__.keys())
        self.assertIn('first_name', self.review4.__dict__.keys())
        self.assertIn('last_name', self.review4.__dict__.keys())
        self.assertEqual(str(self.review4),
                         "[Review] ({}) {}".format(
                             "0e5ad480-ebf5-4bc8-9771-2a0e8daff36d",
                             self.review4.__dict__))
        self.assertNotIn('email', self.review1.__dict__.keys())
        self.assertNotIn('password', self.review1.__dict__.keys())
        self.assertNotIn('first_name', self.review1.__dict__.keys())
        self.assertNotIn('last_name', self.review1.__dict__.keys())
        self.assertNotIn('email', self.review2.__dict__.keys())
        self.assertNotIn('password', self.review2.__dict__.keys())
        self.assertNotIn('first_name', self.review2.__dict__.keys())
        self.assertNotIn('last_name', self.review2.__dict__.keys())

    def test_str_instance_attrs(self):
        self.assertNotIn('number', self.review2.__dict__.keys())
        self.assertIn('number', self.review1.__dict__.keys())

    def test_save(self):
        self.assertEqual(self.review1.updated_at,
                         datetime.datetime(2019, 11, 13, 1, 25, 18, 335279))
        self.review1.save()
        self.assertNotEqual(self.review1.updated_at,
                            datetime.datetime(2019, 11, 13, 1, 25, 18, 335279))
        self.assertEqual(type(self.review1.updated_at), datetime.datetime)

    def test_save_instance_attrs(self):
        self.review1.save()
        self.assertEqual(self.review1.number, 89)

    def test_save_class_attrs(self):
        self.review4.save()
        self.assertEqual(self.review4.first_name, "Betty")
        self.assertEqual(self.review4.last_name, "Holberton")
        self.assertEqual(self.review4.email, "airbnb@holbertonschool.com")
        self.assertEqual(self.review4.password, "root")

    def test_to_dict(self):
        dict1 = {'number': 89,
                 '__class__': "Review",
                 'created_at': "2019-11-13T01:25:18.335269",
                 'updated_at': "2019-11-13T01:25:18.335279",
                 'id': "0e5ad480-ebf5-4bc8-9771-2a0e8daff35d"}
        self.assertEqual(self.review1.to_dict(), dict1)

    def test_to_dict_instance_attrs(self):
        self.review1.astring = "pew! pew pew!!!"
        self.review1.afloat = 9.87654321
        dict1 = {'number': 89,
                 'astring': "pew! pew pew!!!",
                 'afloat': 9.87654321,
                 '__class__': "Review",
                 'created_at': "2019-11-13T01:25:18.335269",
                 'updated_at': "2019-11-13T01:25:18.335279",
                 'id': "0e5ad480-ebf5-4bc8-9771-2a0e8daff35d"}
        self.assertEqual(self.review1.to_dict(), dict1)

    def test_to_dict_class_attrs(self):
        dict4 = {'first_name': "Betty",
                 'last_name': "Holberton",
                 'email': "airbnb@holbertonschool.com",
                 'password': "root",
                 '__class__': "Review",
                 'created_at': "2019-11-13T01:25:18.335289",
                 'updated_at': "2019-11-13T01:25:18.335299",
                 'id': "0e5ad480-ebf5-4bc8-9771-2a0e8daff36d"}
        self.assertEqual(self.review4.to_dict(), dict4)
