import unittest
from Module4.Nestedif.coupon_calculations import calculate_price

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)
def price_under_10(self):
        result = calculate_price(9, 5, 10)
        self.assertEqual(result)
        result = calculate_price(5, 5, 15)
        self.assertEqual(result)
        result = calculate_price(4, 5, 20)
        self.assertEqual(result)
        result = calculate_price(1, 10, 10)

if __name__ == '__main__':
    unittest.main()
