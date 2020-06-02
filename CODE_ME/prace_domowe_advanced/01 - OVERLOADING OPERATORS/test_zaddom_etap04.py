import unittest

from zaddom01 import MyTime


class TestEtap4(unittest.TestCase):
    def test_subtraction(self):
        result = MyTime(10, 10) - MyTime(1, 1)
        self.assertTrue(result == MyTime(9, 9))

        result = MyTime(10, 1) - MyTime(0, 59)
        self.assertTrue(result == MyTime(9, 2))

        result = MyTime(10, 1) - MyTime(1, 0)
        self.assertTrue(result == MyTime(9, 1))

        with self.assertRaises(ValueError):
            result = MyTime(0, 1) - MyTime(0, 2)

        with self.assertRaises(ValueError):
            result = MyTime(0, 3) - MyTime(1, 0)


if __name__ == '__main__':
    unittest.main()
