# tutaj wpisz swoje imię i nazwisko

import time
import random


def timer_dekorator(function):
    # tutaj napisz swój kod
    pass


@timer_dekorator
def example_function():
    for _ in range(10):
        print('.', end='', flush=True)
        time.sleep(random.uniform(0, 0.1))
    print()


if __name__ == '__main__':
    example_function()
