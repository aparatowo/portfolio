# Rafał Nitychoruk

import random

class Deck:
    def __init__(self):
        self._cards = ['2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'J♠', 'Q♠', 'K♠', 'A♠', '2♣', '3♣', '4♣',
                       '5♣', '6♣', '7♣', '8♣', '9♣', '10♣', 'J♣', 'Q♣', 'K♣', 'A♣', '2♥', '3♥', '4♥', '5♥', '6♥', '7♥',
                       '8♥', '9♥', '10♥', 'J♥', 'Q♥', 'K♥', 'A♥', '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', '10♦',
                       'J♦', 'Q♦', 'K♦', 'A♦']

    def __next__(self):
        if self._cards == []:
            raise StopIteration
        random_card = random.choice(self._cards)
        self._cards.remove(random_card)

        return random_card

    def __iter__(self):
        return self

if __name__ == '__main__':
    # tutaj można pisać dowolny kod, nie wpływa to na testy
    deck = Deck()
    for _ in range(52):
        print(next(deck))
    pass
