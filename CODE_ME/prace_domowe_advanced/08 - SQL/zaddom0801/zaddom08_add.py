# tutaj wpisz swoje imie i nazwisko
import sqlite3


def read_new_item():
    name = input('Podaj nazwę przedmiotu: ')
    quantity = input(f'Ile {name} dołożyć do plecaka: ')
    weight = input(f'Waga jednej sztuki {name} (w kg): ')
    type = input('typ przedmiotu: [e]quipment czy [f]ood? ')

    # tutaj sprawdź wpisaną przez użytkownika wartość `type`
    if type == 'e' or type == 'equipment':
        type = 'equipment'
    elif type == 'f' or type == 'food':
        type = 'food'
    else:
        raise ValueError

    return name, quantity, weight, type


def add_items(cursor, name, quantity, weight, type):
    query = """
    INSERT INTO "backpack" ("name", "type", "quantity", "weight") 
    VALUES (:name, :type, :quantity, :weight) 
    """
    item = {"name": name, "type": type, "quantity": quantity, "weight": weight}
    cursor.execute(query)


if __name__ == '__main__':
    conn = sqlite3.connect('zaddom08.db')
    cursor = conn.cursor()

    name, quantity, weight, type = read_new_item()

    add_items(cursor, name, quantity, weight, type)

    conn.commit()
    conn.close()
