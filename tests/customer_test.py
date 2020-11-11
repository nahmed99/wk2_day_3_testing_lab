import unittest
from src.customer import Customer
from src.drink import Drink

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Charlie", 60.0, 25, 4)
        self.drink = Drink("champagne", 30.0, 15)

    
    def test_customer_has_name(self):
        self.assertEqual("Charlie", self.customer.name)


    def test_customer_has_wallet(self):
        self.assertEqual(60.0, self.customer.wallet)


    def test_customer_has_age(self):
        self.assertEqual(25, self.customer.age)


    def test_customer_has_drunkenness(self):
        self.assertEqual(4, self.customer.drunkenness)


    def test_customer_increase_drunkenness(self):
        self.customer.add_drunkeness_to_customer(self.drink)
        self.assertEqual(19, self.customer.drunkenness)
