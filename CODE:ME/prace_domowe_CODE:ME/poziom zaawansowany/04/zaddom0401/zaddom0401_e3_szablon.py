# tutaj wpisz swoje imię i nazwisko

import time
import random


def timer_dekorator(function):
    # tutaj napisz swój kod
    pass


@timer_dekorator
def example_function(rounds=10, verbose=True):
    for _ in range(rounds):
        if verbose:
            print('.', end='', flush=True)
        time.sleep(random.uniform(0, 0.1))
    print()


if __name__ == '__main__':
    example_function()
    example_function(2)
    example_function(3, False)
    example_function(4, verbose=False)
