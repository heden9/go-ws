import unittest
from calc import add, subtract


class TestAdd(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(add(12, 34), 46)

    def test_negative(self):
        self.assertEqual(add(-5, -7), -12)
        self.assertEqual(add(-5, 7), 2)

    def test_zero(self):
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(0, 99), 99)
        self.assertEqual(add(99, 0), 99)

    def test_subtract(self):
        self.assertEqual(subtract(10, 3), 7)
        self.assertEqual(subtract(-5, -7), 2)
        self.assertEqual(subtract(0, 0), 0)
        self.assertEqual(subtract(5, 0), 5)


if __name__ == "__main__":
    unittest.main()
