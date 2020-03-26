import unittest

from zaddom02_e2 import draw_cards, Deck


class Etap2(unittest.TestCase):
    def test_simple_draw(self):
        deck = Deck()

        cards = draw_cards(deck)
        self.assertEqual(len(cards), 1)

    def test_draw_ten_cards(self):
        deck = Deck()

        cards = draw_cards(deck, 10)
        self.assertEqual(len(cards), 10)

    def test_draw_more_than_the_deck(self):
        deck = Deck()

        cards50 = draw_cards(deck, 50)
        cards10 = draw_cards(deck, 10)
        self.assertEqual(len(cards10), 2)

        cards_drawn_from_empty_deck = draw_cards(deck, 10)
        self.assertEqual(len(cards_drawn_from_empty_deck), 0)

    def test_drawing_invalid_number_of_cards(self):
        deck = Deck()

        cards0 = draw_cards(deck, 0)
        self.assertEqual(cards0, [])

        cards_minus = draw_cards(deck, -10)
        self.assertEqual(cards_minus, [])


if __name__ == '__main__':
    unittest.main()
