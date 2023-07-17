import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):

    def setUp(self):
        self.drink_1 = Drink("cider", 4.00)
        self.drink_2 = Drink("cola", 1.50)
        self.pub = Pub("The Clansman")
        self.customer = Customer("Winston", 30)

    def test_pub_has_name(self):
        self.assertEqual("he Clansman", self.pub.name)
        

        