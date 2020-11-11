import unittest
from src.pub import Pub
from src.drink import Drink

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("The Red Lion", 50.0)
        self.drink_1 = Drink("tea", 0.95)
        
    
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


    def test_find_drink_by_name(self):
        self.pub.add_drink(Drink("champagne", 30.0))
        self.pub.add_drink(Drink("lemonade", 1.95))
        self.pub.add_drink(Drink("negroni", 7.95))

        drink_found = self.pub.find_drink_by_name("lemonade")
        drink_not_found = self.pub.find_drink_by_name("hot chocolate")
        self.assertEqual("lemonade", drink_found.name)
        self.assertIsNone(drink_not_found)


    def test_add_money_to_till(self):
        self.pub.add_money_to_till(self.drink_1)
        self.assertEqual(50.95, self.pub.get_till_total())

