import unittest

from zaddom01 import MyTime


class TestEtap2(unittest.TestCase):
    def test_equality(self):
        self.assertTrue(MyTime(3, 3) > MyTime(3, 2))
        self.assertTrue(MyTime(3, 3) > MyTime(2, 2))
        self.assertTrue(MyTime(2, 3) > MyTime(2, 2))
        self.assertFalse(MyTime(2, 2) > MyTime(2, 2))

        self.assertFalse(MyTime(3, 3) < MyTime(3, 2))
        self.assertFalse(MyTime(3, 3) < MyTime(2, 2))
        self.assertFalse(MyTime(2, 3) < MyTime(2, 2))
        self.assertFalse(MyTime(2, 2) < MyTime(2, 2))

        self.assertTrue(MyTime(1, 1) == MyTime(1, 1))
        self.assertTrue(MyTime(0, 1) != MyTime(0, 2))
        self.assertTrue(MyTime(1, 1) != MyTime(0, 1))


if __name__ == '__main__':
    unittest.main()
