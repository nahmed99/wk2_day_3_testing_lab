import unittest
from src.pub import Pub
#from src.bus_stop import BusStop
#from src.person import Person

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("The Red Lion", 50.0)

    
    def test_pub_has_name(self):
        self.assertEqual("The Red Lion", self.pub.name)


    
    # def test_has_destination(self):
    #     self.assertEqual("Ocean Terminal", self.bus.destination)
