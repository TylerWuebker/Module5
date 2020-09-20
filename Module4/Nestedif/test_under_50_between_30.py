import unittest
from Module4.Nestedif.coupon_calculations import calculate_price

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)
    def price_under_between_30_50(self):
        result = calculate_price(35, 5, 10)
        self.assertEqual(result)
        result = calculate_price(30, 5, 15)
        self.assertEqual(result)
        result = calculate_price(40, 5, 20)
        self.assertEqual(result)
        result = calculate_price(45, 10, 10)

if __name__ == '__main__':
    unittest.main()
