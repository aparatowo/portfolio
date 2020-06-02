import sqlite3
import unittest
import sys
from contextlib import contextmanager
from io import StringIO
from unittest.mock import patch

from zaddom08_add import read_new_item, add_items
from zaddom08_db_init import initialize_db
from zaddom08_info import print_equipment, print_food, print_backpack_weight


@contextmanager
def captured_output():
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


class Zaddom09ReadNewItem(unittest.TestCase):

    def test_short_names(self):
        with patch('builtins.input', side_effect=['name', 1, 1, 'e']):
            _, _, _, type_ = read_new_item()
            self.assertEqual('equipment', type_)

        with patch('builtins.input', side_effect=['name', 1, 1, 'f']):
            _, _, _, type_ = read_new_item()
            self.assertEqual('food', type_)

    def test_full_names(self):
        with patch('builtins.input', side_effect=['name', 1, 1, 'equipment']):
            _, _, _, type = read_new_item()
            self.assertEqual('equipment', type)

        with patch('builtins.input', side_effect=['name', 1, 1, 'food']):
            _, _, _, type = read_new_item()
            self.assertEqual('food', type)

    def test_wrong_type(self):
        with patch('builtins.input', side_effect=['name', 1, 1, 'wrong_type']):
            with self.assertRaises(ValueError):
                read_new_item()


class Zaddom09AddItem(unittest.TestCase):
    def test_successful_item_addition(self):
        conn = sqlite3.connect(':memory:')
        cursor = conn.cursor()

        initialize_db(cursor)

        name, quantity, weight, type = 'name', 1, 1, 'equipment'
        add_items(cursor, name, quantity, weight, type)

        conn.commit()
        cursor.execute("SELECT * FROM backpack")
        result = cursor.fetchall()

        expected = [(1, 'name', 'equipment', 1, 1.0)]

        self.assertEqual(expected, result)


class Zaddom09Info(unittest.TestCase):

    def setUp(self):
        self.conn = sqlite3.connect(':memory:')
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()

        initialize_db(self.cursor)
        script = """
            INSERT INTO "backpack" VALUES (NULL, 'c', 'equipment', 1, 1);
            INSERT INTO "backpack" VALUES (NULL, 'a', 'equipment', 10, 2);
            INSERT INTO "backpack" VALUES (NULL, 'b', 'equipment', 100, 3);
            INSERT INTO "backpack" VALUES (NULL, 'f', 'food', 1, 0.1);
            INSERT INTO "backpack" VALUES (NULL, 'd', 'food', 1, 0.2);
            INSERT INTO "backpack" VALUES (NULL, 'e', 'food', 1, 0.3);
        """
        self.cursor.executescript(script)
        self.conn.commit()

    def tearDown(self):
        self.conn.close()

    def test_print_equipment(self):
        with captured_output() as (out, err):
            print_equipment(self.cursor)
            output = out.getvalue()

        self.assertIn('a\nb\nc\n', output)

    def test_print_food(self):
        with captured_output() as (out, err):
            print_food(self.cursor)
            output = out.getvalue()

        self.assertIn('d\ne\nf\n', output)

    def test_print_backpack_weight(self):
        with captured_output() as (out, err):
            print_backpack_weight(self.cursor)
            output = out.getvalue()

        self.assertIn('Waga zawartości: 321.6kg\n', output)


if __name__ == '__main__':
    unittest.main()
