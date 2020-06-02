# tutaj wpisz swoje imie i nazwisko
import sqlite3


def read_new_item():
    name = input('Podaj nazwę przedmiotu: ')
    quantity = input(f'Ile {name} dołożyć do plecaka: ')
    weight = input(f'Waga jednej sztuki {name} (w kg): ')
    type = input('typ przedmiotu: [e]quipment czy [f]ood? ')

    # tutaj sprawdź wpisaną przez użytkownika wartość `type`

    return name, quantity, weight, type


def add_items(cursor, name, quantity, weight, type):
    pass  # tutaj stwórz i wywołaj zapytanie SQL


if __name__ == '__main__':
    conn = sqlite3.connect('zaddom09.db')
    cursor = conn.cursor()

    name, quantity, weight, type = read_new_item()

    add_items(cursor, name, quantity, weight, type)

    conn.commit()
    conn.close()
