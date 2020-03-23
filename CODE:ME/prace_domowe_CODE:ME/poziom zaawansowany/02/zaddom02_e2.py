# Rafał Nitychoruk

from zaddom02_e1 import Deck


def draw_cards(deck, amount=1):
    picked_cards = []

    for _ in range(amount):
        try:
            picked_card = next(deck)
            picked_cards.append(picked_card)
        except StopIteration:
            break

    return picked_cards


if __name__ == '__main__':
    deck = Deck()

    player1 = draw_cards(deck, 16)
    player2 = draw_cards(deck, 4)
    player3 = draw_cards(deck, 17)
    player4 = draw_cards(deck, 23)

    print(player1)
    print(player2)
    print(player3)
    print(player4)
