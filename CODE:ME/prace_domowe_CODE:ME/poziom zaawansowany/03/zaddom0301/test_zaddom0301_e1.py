import unittest
from zaddom0301_e1 import strip_extensions


class Etap1(unittest.TestCase):
    def test_single_extension(self):
        files = ['spreadsheet.xlsx', 'music.mp3']
        result = strip_extensions(files)
        expected = ['spreadsheet', 'music']

        self.assertEqual(expected, result)

    def test_double_extension(self):
        files = ['archive.tar.gz']
        result = strip_extensions(files)
        expected = ['archive']

        self.assertEqual(expected, result)

    def test_no_extension(self):
        files = ['temp']
        result = strip_extensions(files)
        expected = ['temp']

        self.assertEqual(expected, result)

    def test_no_file(self):
        files = [None]
        result = strip_extensions(files)
        expected = []

        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
