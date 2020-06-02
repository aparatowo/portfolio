from contextlib import contextmanager
import unittest
from io import StringIO
from unittest.mock import patch, mock_open
import sys

from zaddom10 import main
MODULE_NAME = 'zaddom10'

EXAMPLE_TEXT = '''this is
an example
text
'''

FILENAME = 'zen.txt'


@contextmanager
def captured_output():
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


def run_main_with_cmd_args(args=None):
    full_args = [sys.argv[0]]

    if args is not None:
        full_args.extend(args)

    with captured_output() as (out, err):
        with patch('sys.argv', full_args):
            exit_code = None
            try:
                main()
            except SystemExit as e:
                exit_code = e.code
        out_val = out.getvalue()
        err_val = err.getvalue()

    return out_val, err_val, exit_code


class Zaddom10(unittest.TestCase):

    @patch('builtins.open', mock_open(read_data=EXAMPLE_TEXT))
    def test_set_log_level_default(self):
        out, err, _ = run_main_with_cmd_args([FILENAME])
        self.assertIn('4 5 24 zen.txt', out)
        self.assertNotIn('INFO', err)
        self.assertNotIn('DEBUG', err)

    @patch('builtins.open', mock_open(read_data=EXAMPLE_TEXT))
    def test_set_log_level_correct_level(self):
        possible_args = ['-v', '--log-level']

        level = 'DEBUG'
        for arg in possible_args:
            with self.subTest(f'test for {arg} {level}'):
                out, err, _ = run_main_with_cmd_args([arg, level, FILENAME])
                self.assertIn('4 5 24 zen.txt', out)
                self.assertIn('INFO', err)
                self.assertIn('DEBUG', err)

        level = 'INFO'
        for arg in possible_args:
            with self.subTest(f'test for {arg} {level}'):
                out, err, _ = run_main_with_cmd_args([arg, level, FILENAME])
                self.assertIn('4 5 24 zen.txt', out)
                self.assertNotIn('DEBUG', err)
                self.assertIn('INFO', err)

        level = 'WARNING'
        for arg in possible_args:
            with self.subTest(f'test for {arg} {level}'):
                out, err, _ = run_main_with_cmd_args([arg, level, FILENAME])
                self.assertIn('4 5 24 zen.txt', out)
                print(err)
                self.assertNotIn('DEBUG', err)
                self.assertNotIn('INFO', err)

    def test_set_log_level_invalid_level(self):
        possible_args = ['-v', '--log-level']

        level = 'INVALID_LEVEL'
        for arg in possible_args:
            with self.subTest(f'test for {arg} {level}'):
                out, err, code = run_main_with_cmd_args([arg, level, FILENAME])
                self.assertIn("invalid choice: 'INVALID_LEVEL'", err)
                self.assertEqual(2, code)

    @patch('zaddom10_functions.open_file', return_value=EXAMPLE_TEXT)
    @patch(f'{MODULE_NAME}.wc')
    def test_filename_passed_without_other_args(self, patched_wc, _):
        run_main_with_cmd_args([FILENAME])
        patched_wc.assert_called_with(FILENAME, 'full')

    @patch('zaddom10_functions.open_file', return_value=EXAMPLE_TEXT)
    @patch(f'{MODULE_NAME}.wc')
    def test_filename_passed_with_log_level_args(self, patched_wc, _):
        run_main_with_cmd_args(['-v', 'DEBUG', FILENAME])
        patched_wc.assert_called_with(FILENAME, 'full')

    @patch('builtins.open', side_effect=FileNotFoundError)
    def test_file_not_found(self, _):
        out, err, code = run_main_with_cmd_args([FILENAME])
        self.assertIn('WARNING', err)
        self.assertIn('nie znaleziono pliku', err)


if __name__ == '__main__':
    unittest.main()
