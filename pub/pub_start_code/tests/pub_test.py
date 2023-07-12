import unittest
from src.pub import Pub
from src.drink import Drink

class TestPub(unittest.TestCase):

    def setUp(self):
        self.lager = Drink("Tennents", 3.50)
        self.wine = Drink("House Red", 4.25)

        self.drinks = [self.lager, self.wine]

        