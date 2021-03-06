import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("flat white", 2.5, 0)

    
    def test_drink_has_name(self):
        self.assertEqual("flat white", self.drink.name)


    def test_drink_has_price(self):
        self.assertEqual(2.5, self.drink.price)


    def test_drink_has_alcohol_level(self):
        self.assertEqual(0, self.drink.alcohol_level)


    