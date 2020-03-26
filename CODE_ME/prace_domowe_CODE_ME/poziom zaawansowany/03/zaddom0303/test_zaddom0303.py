import unittest
import types
from zaddom0303 import counter_generator


class Etap1(unittest.TestCase):
    def test_function_creates_a_generator(self):
        counter = counter_generator()

        self.assertEqual(type(counter), types.GeneratorType)

    def test_first_three_values(self):
        counter = counter_generator()

        number = next(counter)
        self.assertEqual(number, '00')

        number = next(counter)
        self.assertEqual(number, '01')

        number = next(counter)
        self.assertEqual(number, '02')

    def test_with_start_value(self):
        START_VALUE = 13
        counter = counter_generator(START_VALUE)

        number = next(counter)
        self.assertEqual(number, str(START_VALUE))

    def test_start_from_beginning(self):
        counter = counter_generator()

        for i in range(10):
            number = next(counter)
            self.assertEqual(number, '00')

            for _ in range(98):
                next(counter)

            number = next(counter)
            self.assertEqual(number, '99')


if __name__ == '__main__':
    unittest.main()
