import unittest

from zaddom02_e1 import Deck


class Etap1(unittest.TestCase):
    def test_draw_one_draw(self):
        deck = Deck()

        card = next(deck)
        self.assertEqual(len(deck._cards), 51)

    def test_draw_every_card(self):
        deck = Deck()
        every_card = set(deck)

        self.assertEqual(len(every_card), 52)

    def test_exhausing_the_deck(self):
        deck = Deck()

        with self.assertRaises(StopIteration):
            for _ in range(53):
                next(deck)

    def test_if_drawing_is_random(self):
        for _ in range(100):
            deck1 = Deck()
            deck2 = Deck()
            if next(deck1) != next(deck2):
                return
        self.fail()


if __name__ == '__main__':
    unittest.main()
