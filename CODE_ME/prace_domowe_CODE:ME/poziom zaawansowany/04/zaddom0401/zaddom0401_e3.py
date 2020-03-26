# tutaj wpisz swoje imię i nazwisko

import time
import random
from datetime import datetime


def timer_dekorator(function, *args, **kwargs):
    def wrap(*args, **kwargs):
        t1 = datetime.now()
        function(*args, **kwargs)
        t2 = datetime.now()
        t3 = t2 - t1
        print(f'Czas wykonania: {t3}')
    return wrap



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
