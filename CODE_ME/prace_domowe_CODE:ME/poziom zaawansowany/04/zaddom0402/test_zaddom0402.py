import unittest
from zaddom0402 import generate_email_addresses

NOTACTIVEID = 80
ACTIVEID = 72
EMAILHOST = 'test.pl'
PEOPLE = [
    {'id': ACTIVEID, 'imie': 'Jakub', 'nazwisko': 'Malinowski', 'active': True},
    {'id': NOTACTIVEID, 'imie': 'Jadwiga', 'nazwisko': 'Brzezińska', 'active': False},
]


class Zaddom0402(unittest.TestCase):
    def setUp(self):
        self.output = generate_email_addresses(PEOPLE, EMAILHOST)

    def test_non_active_users_filtered_out(self):
        self.assertNotIn(NOTACTIVEID, self.output)

    def test_active_person_has_correct_email(self):
        self.assertEqual(self.output[ACTIVEID], 'jmalinowski@test.pl')

    def test_correct_length_of_output(self):
        self.assertEqual(len(self.output), 1)


if __name__ == '__main__':
    unittest.main()
