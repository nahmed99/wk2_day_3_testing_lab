import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Charlie", 60.0)

    
    def test_customer_has_name(self):
        self.assertEqual("Charlie", self.customer.name)


    def test_customer_has_wallet(self):
        self.assertEqual(60.0, self.customer.wallet)