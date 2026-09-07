import unittest
from calc import add


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


if __name__ == "__main__":
    unittest.main()
