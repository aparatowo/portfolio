# tutaj wpisz swoje imię i nazwisko


def number_of_digits(numbers):
    tuples = [(number, len(str(number).strip('-'))) for number in numbers]
    return tuples


if __name__ == '__main__':
    numbers = [91111, -7108079251, 4, 7942725602, -345220, 2915371507, -30, 9438104, 5736286, 984, 0]
    print(number_of_digits(numbers))
