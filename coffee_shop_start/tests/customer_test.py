import unittest
from src.customer import Customer
from src.drink import Drink

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.paul = Customer("Paul", 50)
        self.water = Drink("Spring Water", 10)

    def test_customer_has_name(self):
        expected = "Paul"
        actual = self.paul.name
        self.assertEqual(expected, actual)

    def test_cusotmer_has_wallet(self):
        self.assertEqual(50, self.paul.wallet)

    def test_customer_can_buy_drink(self):
        self.customer.buy_drink(self.water)
        self.assertEqual(40, self.paul.wallet)
        