import unittest
from zaddom0301_e2 import number_of_digits


class Etap1(unittest.TestCase):
    def test_positive_numbers(self):
        numbers = [0, 12, 222, 3333]
        result = number_of_digits(numbers)
        expected = [(0, 1), (12, 2), (222, 3), (3333, 4)]

        self.assertEqual(expected, result)

    def test_negative_numbers(self):
        numbers = [0, -1, -222, -12345]
        result = number_of_digits(numbers)
        expected = [(0, 1), (-1, 1), (-222, 3), (-12345, 5)]

        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
