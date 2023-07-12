import unittest
from src.customer import Customer
from src.drink import Drink

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.pippin = Customer("Pippin", 50)

    def test_customer_has_name(self):
        expected = "Pippin"
        actual = self.pippin.name
        self.assertEqual(expected, actual)
    
    def test_customer_has_wallet(self):
        self.assertEqual(50, self.pippin.wallet)

    
    