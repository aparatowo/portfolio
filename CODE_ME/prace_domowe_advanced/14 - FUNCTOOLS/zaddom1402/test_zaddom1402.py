import sys
import unittest
from contextlib import contextmanager
from io import StringIO

STRING = '''eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
e                                                               e
e     ddddddddddddddddddddddddddddddddddddddddddddddddddddd     e
e     d                                                   d     e
e     d     ccccccccccccccccccccccccccccccccccccccccc     d     e
e     d     c                                       c     d     e
e     d     c     bbbbbbbbbbbbbbbbbbbbbbbbbbbbb     c     d     e
e     d     c     b                           b     c     d     e
e     d     c     b     aaaaaaaaaaaaaaaaa     b     c     d     e
e     d     c     b     a               a     b     c     d     e
e     d     c     b     a     Dzień     a     b     c     d     e
e     d     c     b     a     Dobry     a     b     c     d     e
e     d     c     b     a               a     b     c     d     e
e     d     c     b     aaaaaaaaaaaaaaaaa     b     c     d     e
e     d     c     b                           b     c     d     e
e     d     c     bbbbbbbbbbbbbbbbbbbbbbbbbbbbb     c     d     e
e     d     c                                       c     d     e
e     d     ccccccccccccccccccccccccccccccccccccccccc     d     e
e     d                                                   d     e
e     ddddddddddddddddddddddddddddddddddddddddddddddddddddd     e
e                                                               e
eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee'''


@contextmanager
def captured_output():
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


class TestZaddom1101Etap1(unittest.TestCase):

    def test_correct_output(self):
        with captured_output() as (out, err):
            import zaddom1402
            self.assertIn(STRING, out.getvalue())

    def test_less_than_six_lines(self):
        with open('zaddom1402.py') as f:
            lines = filter(lambda line: line != '\n' and not line.startswith('#'), f.readlines())

            self.assertLessEqual(len(list(lines)), 6)