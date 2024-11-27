# test_main.py

import unittest
from main import add, subtract, multiply, divide, modulus

class TestArithmeticOperations(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(add(10, 5), 15)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(5, 10), -5)
        self.assertEqual(subtract(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(multiply(10, 5), 50)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(0, 10), 0)

    def test_divide(self):
        self.assertEqual(divide(10, 5), 2)
        self.assertEqual(divide(1, 3), 1 / 3)
        self.assertEqual(divide(0, 1), 0)
        self.assertEqual(divide(10, 0), "Error: Division by zero is not allowed.")

    def test_modulus(self):
        self.assertEqual(modulus(10, 3), 1)
        self.assertEqual(modulus(10, 5), 0)
        self.assertEqual(modulus(0, 5), 0)
        self.assertEqual(modulus(10, 0), "Error: Modulus by zero is not allowed.")

if __name__ == "__main__":
    unittest.main()