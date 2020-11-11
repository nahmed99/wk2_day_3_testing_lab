import unittest
from src.pub import Pub

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("The Red Lion", 50.0)

    
    def test_pub_has_name(self):
        self.assertEqual("The Red Lion", self.pub.name)


    def test_pub_has_till(self):
         self.assertEqual(50.0, self.pub.till)


    def test_drinks_list_starts_empty(self):
        self.assertEqual(0, self.pub.drinks_list_length())
