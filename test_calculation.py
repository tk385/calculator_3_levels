# tests/test_calculation.py

import unittest
from calculation import Calculation

class TestCalculation(unittest.TestCase):
    def test_creation(self):
        calc = Calculation("+", 5, 3, 8)
        self.assertEqual(calc.operation, "+")
        self.assertEqual(calc.x, 5)
        self.assertEqual(calc.y, 3)
        self.assertEqual(calc.result, 8)

    def test_representation(self):
        calc = Calculation("+", 5, 3, 8)
        self.assertEqual(repr(calc), "5 + 3 = 8")

if __name__ == "__main__":
    unittest.main()