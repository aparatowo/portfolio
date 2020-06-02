#Rafał Nitychoruk
import sqlite3
from functools import reduce
from decimal import *


def print_equipment(cursor):
    query = """
    SELECT "name" FROM "backpack" where "type" = "equipment" ORDER BY "name" ASC;
    """
    cursor.execute(query)
    items = cursor.fetchall()
    for name in items:
        print(name[0])


def print_food(cursor):
    query = """SELECT name FROM "backpack" WHERE "type" = "food" ORDER BY "name" ASC;"""
    cursor.execute(query)
    items = cursor.fetchall()
    for name in items:
        print(name[0])


def print_backpack_weight(cursor):
    query = """SELECT weight FROM "backpack";"""

    cursor.execute(query)
    weight = cursor.fetchall()

    sum_weight = [float(item[0]) for item in weight]
    sum_weight = sum(sum_weight)

    print(f'Waga zawartości: {sum_weight}kg')

if __name__ == '__main__':
    conn = sqlite3.connect('zaddom08.db')
    cursor = conn.cursor()

    print('Sprzęt:')
    print_equipment(cursor)
    print()

    print('Jedzenie:')
    print_food(cursor)
    print()

    print_backpack_weight(cursor)

    conn.close()
