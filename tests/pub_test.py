import unittest
from src.pub import Pub
from src.drink import Drink

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("The Red Lion", 50.0)
        
    
    def test_pub_has_name(self):
        self.assertEqual("The Red Lion", self.pub.name)


    def test_pub_has_till(self):
         self.assertEqual(50.0, self.pub.till)


    def test_drinks_list_starts_empty(self):
        self.assertEqual(0, self.pub.drinks_list_length())


    def test_add_drink(self):
        self.pub.add_drink(Drink("champagne", 30.0))
        self.pub.add_drink(Drink("lemonade", 1.95))
        self.pub.add_drink(Drink("negroni", 7.95))

        self.assertEqual(3, self.pub.drinks_list_length())
