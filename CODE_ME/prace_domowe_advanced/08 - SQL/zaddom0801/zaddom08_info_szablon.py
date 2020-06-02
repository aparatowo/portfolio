# tutaj wpisz swoje imie i nazwisko
import sqlite3


def print_equipment(cursor):
    query = ''  # uzupełnij

    # kod wypisujący sprzęty


def print_food(cursor):
    query = ''  # uzupełnij

    # kod wypisujący jedzenie


def print_backpack_weight(cursor):
    query = ''  # uzupełnij

    # kod obliczający sumaryczną wagę przedmiotów

    sum_weight = 0
    print(f'Waga zawartości: {sum_weight}kg')


if __name__ == '__main__':
    conn = sqlite3.connect('zaddom09.db')
    cursor = conn.cursor()

    print('Sprzęt:')
    print_equipment(cursor)
    print()

    print('Jedzenie:')
    print_food(cursor)
    print()

    print_backpack_weight(cursor)

    conn.close()
