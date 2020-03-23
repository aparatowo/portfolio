import unittest
import sys
from contextlib import contextmanager
from io import StringIO

from zaddom0401_e2 import example_function


@contextmanager
def captured_output():
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


class Zaddom0401_e2(unittest.TestCase):
    def test_correct_output(self):
        with captured_output() as (out, err):
            example_function()

            output = out.getvalue().strip()
        timer_output = output.split('\n')[1]

        self.assertEqual(timer_output[:22], 'Czas wykonania: 0:00:0')

        seconds = float(timer_output[22:])
        self.assertGreater(seconds, 0)
        self.assertLessEqual(seconds, 1)


if __name__ == '__main__':
    unittest.main()
